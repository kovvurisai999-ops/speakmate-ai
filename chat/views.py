import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import ChatMessage
from ai_engine.gemini import gemini_ai
from ai_engine.tts import TTSEngine
import uuid

# Initialize TTS
tts_engine = TTSEngine()

@login_required
def chat_index(request):
    messages = ChatMessage.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'chat/index.html', {
        'history': messages,
        'LOCAL_MODE': True,
        'OPENAI_API_KEY': settings.OPENAI_API_KEY if settings.OPENAI_API_KEY != "your_openai_api_key_here" else None
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_text = data.get('message', '')
            user = request.user
            
            # Integrated Settings into System Prompt
            system_prompt = (
                f"You are an expert English Coach with a {user.ai_personality} personality. "
                f"The student's difficulty level is {user.ai_difficulty} and preferred language is {user.preferred_language}.\n"
                "Analyze the user input:\n"
                f"1. If it's in {user.preferred_language}, translate it to natural English.\n"
                "2. Check the grammar and give a short tip.\n"
                "3. Give a friendly reply matching your assigned personality.\n"
                "Output exactly in this format:\n"
                "ENGLISH: [The full English translation]\n"
                "TIP: [A short grammar tip]\n"
                "REPLY: [Your conversational reply]"
            )
            
            full_content = gemini_ai.ask(system_prompt, user_text, max_tokens=500)
            
            # Line-based Parsing
            translated_text = user_text
            grammar_feedback = "Analyzed!"
            ai_reply = full_content

            for line in full_content.split('\n'):
                line = line.strip()
                if line.startswith('ENGLISH:'):
                    translated_text = line.replace('ENGLISH:', '').strip()
                elif line.startswith('TIP:'):
                    grammar_feedback = line.replace('TIP:', '').strip()
                elif line.startswith('REPLY:'):
                    ai_reply = line.replace('REPLY:', '').strip()
            
            # Fallback split
            if ai_reply == full_content and 'REPLY:' in full_content:
                try: ai_reply = full_content.split('REPLY:')[1].strip()
                except: pass

            # 4. Local TTS (Dynamic Voice & Speed)
            audio_url = None
            try:
                filename = f"reply_{uuid.uuid4().hex}.mp3"
                audio_url = tts_engine.save_to_file(
                    ai_reply, 
                    filename, 
                    voice_pref=user.ai_voice, 
                    speed_pref=user.speaking_speed
                )
            except Exception as e:
                print(f"TTS Error: {e}")

            # 5. Save to DB
            chat_msg = ChatMessage.objects.create(
                user=user,
                content=user_text,
                response=ai_reply,
                feedback=grammar_feedback
            )

            return JsonResponse({
                'response': ai_reply,
                'feedback': grammar_feedback,
                'translated': translated_text if translated_text != user_text else None,
                'audio_url': audio_url
            })
        except Exception as e:
            print(f"GLOBAL ERROR in send_message: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
