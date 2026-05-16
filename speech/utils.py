import os
from django.conf import settings

# Explicitly add FFmpeg to PATH for Windows
ffmpeg_path = r"C:\Users\hmind\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"
if ffmpeg_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + ffmpeg_path

class SpeechManager:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            try:
                import whisper
                print("Loading Whisper model...")
                cls._model = whisper.load_model(settings.WHISPER_MODEL)
            except Exception as e:
                print(f"FAILED TO LOAD WHISPER: {e}")
                return None
        return cls._model

    def transcribe(self, audio_path):
        model = self.get_model()
        if model is None:
            return "[AI Transcription Offline due to DLL error. Please check system logs.]", "en"
        
        result = model.transcribe(audio_path)
        return result["text"], result.get("language", "en")
