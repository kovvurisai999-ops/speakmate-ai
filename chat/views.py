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
            print(f"DEBUG: Processing message: {user_text}")
            
            # Line-based markers - The most reliable way
            system_prompt = (
                "You are an expert English Coach. Analyze the user input.\n"
                "1. If it's in Telugu, translate it to natural English.\n"
                "2. Check the grammar and give a short tip.\n"
                "3. Give a friendly reply.\n"
                "Output exactly in this format:\n"
                "ENGLISH: [The full English translation]\n"
                "TIP: [A short grammar tip]\n"
                "REPLY: [Your warm conversational reply]"
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
            
            # Ensure ai_reply is not just the whole content if we found a specific reply
            if ai_reply == full_content and 'REPLY:' in full_content:
                # Fallback split if line-based failed (e.g. no newline)
                try:
                    ai_reply = full_content.split('REPLY:')[1].strip()
                except:
                    pass

            # 4. Local TTS (Voice)
            audio_url = None
            try:
                filename = f"reply_{uuid.uuid4().hex}.mp3"
                audio_url = tts_engine.save_to_file(ai_reply, filename)
            except Exception as e:
                print(f"TTS Error: {e}")

            # 5. Save to DB
            chat_msg = ChatMessage.objects.create(
                user=request.user,
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
