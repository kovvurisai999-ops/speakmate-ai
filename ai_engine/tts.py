import os
from django.conf import settings

class TTSEngine:
    def __init__(self):
        self.enabled = False
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            # Set property before adding anything to speak
            self.engine.setProperty('rate', 150)    # Speed percent (can go over 100)
            self.engine.setProperty('volume', 0.9)  # Volume 0-1
            
            # Select female voice if available
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if "female" in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
            self.enabled = True
        except Exception as e:
            print(f"TTS Engine Initialization Failed: {e}. Offline voice features will be disabled on this platform.")
            self.enabled = False

    def save_to_file(self, text, filename):
        if not self.enabled:
            return None

        path = os.path.join(settings.MEDIA_ROOT, 'tts', filename)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
            
        try:
            # Re-initialize engine for thread safety
            import pyttsx3
            temp_engine = pyttsx3.init()
            temp_engine.setProperty('rate', 150)
            temp_engine.save_to_file(text, path)
            temp_engine.runAndWait()
            # Clean up
            del temp_engine
            return os.path.join(settings.MEDIA_URL, 'tts', filename)
        except Exception as e:
            print(f"TTS Save to File Failed: {e}")
            return None

