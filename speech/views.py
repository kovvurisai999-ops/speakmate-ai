import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .utils import SpeechManager

speech_manager = SpeechManager()

@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        file_name = default_storage.save('temp_audio/' + audio_file.name, audio_file)
        file_path = default_storage.path(file_name)
        
        try:
            text, language = speech_manager.transcribe(file_path)
            # Cleanup
            os.remove(file_path)
            
            return JsonResponse({
                'text': text,
                'language': language
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'No audio file found'}, status=400)
