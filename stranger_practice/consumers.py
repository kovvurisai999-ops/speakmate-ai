import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import OnlineUser, ConversationSession
import random
import string

User = get_user_model()

class MatchmakingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_anonymous:
            await self.close()
            return

        await self.accept()
        
        # Mark user as online and looking
        await self.set_online_status(True)
        
        # Try to find a match
        match = await self.find_match()
        
        if match:
            room_id = self.generate_room_id()
            # Notify both users
            await self.channel_layer.group_add(room_id, self.channel_name)
            
            # We need to tell the other user to join this room too
            # For simplicity in Phase 1, we use a global broadcast to matched users
            await self.channel_layer.group_send(
                f"user_{match.id}",
                {
                    "type": "match_found",
                    "room_id": room_id,
                    "partner_name": self.user.username
                }
            )
            
            await self.send(json.dumps({
                "type": "match_found",
                "room_id": room_id,
                "partner_name": match.username
            }))
        else:
            # Join their own private group to receive match notifications
            await self.channel_layer.group_add(f"user_{self.user.id}", self.channel_name)
            await self.send(json.dumps({
                "type": "searching",
                "message": "Looking for an English practice partner..."
            }))

    async def disconnect(self, close_code):
        if hasattr(self, 'user'):
            await self.set_online_status(False)
            await self.channel_layer.group_discard(f"user_{self.user.id}", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        msg_type = data.get("type")

        if msg_type == "signal":
            # Forward WebRTC signaling data
            room_id = data.get("room_id")
            await self.channel_layer.group_send(
                room_id,
                {
                    "type": "webrtc_signal",
                    "data": data.get("data"),
                    "sender_id": self.user.id
                }
            )
        
        elif msg_type == "virtual_match":
            # Join the virtual room group so feedback messages are received
            room_id = f"virtual_{self.user.id}"
            await self.channel_layer.group_add(room_id, self.channel_name)
            
            await self.send(json.dumps({
                "type": "match_found",
                "room_id": room_id,
                "partner_name": "AI Partner (Virtual)"
            }))
        
        elif msg_type == "speech_text":
            # Analyze grammar in real-time
            text = data.get("text")
            room_id = data.get("room_id")
            analysis = await self.analyze_grammar(text)
            
            await self.channel_layer.group_send(
                room_id,
                {
                    "type": "live_feedback",
                    "sender_name": self.user.username,
                    "original": text,
                    "feedback": analysis
                }
            )

    async def match_found(self, event):
        # Join the assigned room
        await self.channel_layer.group_add(event["room_id"], self.channel_name)
        await self.send(json.dumps({
            "type": "match_found",
            "room_id": event["room_id"],
            "partner_name": event["partner_name"]
        }))

    async def webrtc_signal(self, event):
        # Don't send signal back to self
        if event["sender_id"] != self.user.id:
            await self.send(json.dumps({
                "type": "webrtc_signal",
                "data": event["data"]
            }))

    async def live_feedback(self, event):
        await self.send(json.dumps({
            "type": "live_feedback",
            "sender_name": event["sender_name"],
            "original": event["original"],
            "feedback": event["feedback"]
        }))

    @database_sync_to_async
    def analyze_grammar(self, text):
        from grammar.utils import GrammarChecker
        checker = GrammarChecker()
        corrections, feedback, is_valid = checker.check(text)
        return {"feedback": feedback, "is_valid": is_valid}

    @database_sync_to_async
    def set_online_status(self, status):
        online_user, _ = OnlineUser.objects.get_or_create(user=self.user)
        online_user.is_looking = status
        online_user.save()

    @database_sync_to_async
    def find_match(self):
        # Simple logic: find another user who is looking and is not self
        others = OnlineUser.objects.filter(is_looking=True).exclude(user=self.user).order_by('?')
        if others.exists():
            match = others.first()
            # Once matched, both are no longer "looking" for a new match
            match.is_looking = False
            match.save()
            
            # Note: self status will be set to False when they join the room or via disconnect
            return match.user
        return None

    def generate_room_id(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
