import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .utils import PronunciationAnalyzer

analyzer = PronunciationAnalyzer()

def pronunciation_index(request):
    return render(request, 'pronunciation/index.html')

@csrf_exempt
def analyze_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        target_text = request.POST.get('target_text', '') # Get the text user was supposed to say
        
        file_name = default_storage.save('temp_pron/' + audio_file.name, audio_file)
        file_path = default_storage.path(file_name)
        
        try:
            results = analyzer.analyze(file_path, target_text)
            # Cleanup
            os.remove(file_path)
            
            return JsonResponse(results)
        except Exception as e:
            if os.path.exists(file_path):
                os.remove(file_path)
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'No audio file found'}, status=400)
