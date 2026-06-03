import os
from difflib import SequenceMatcher
from speech.utils import SpeechManager # Reuse our existing local Whisper model

# Explicitly add FFmpeg to PATH for Windows
ffmpeg_path = r"C:\Users\hmind\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"
if ffmpeg_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + ffmpeg_path

class PronunciationAnalyzer:
    def analyze(self, audio_path, target_text):
        try:
            print(f"Analyzing audio: {audio_path}")
            # 1. Transcribe using our local Whisper
            manager = SpeechManager()
            transcription, _ = manager.transcribe(audio_path)
            transcription = transcription.lower().strip()
            
            # Use a safe way to print to Windows terminal
            try:
                print(f"Transcription: {transcription.encode('ascii', 'ignore').decode('ascii')}")
            except:
                print("Transcription contains special characters.")
            
            clean_target = target_text.lower().strip().replace('"', '').replace('.', '').replace(',', '').replace('?', '').replace('!', '')
            clean_trans = transcription.replace('"', '').replace('.', '').replace(',', '').replace('?', '').replace('!', '')

            # 2. Compare transcription with target text (Pronunciation Score)
            matcher = SequenceMatcher(None, clean_trans, clean_target)
            pron_score = int(matcher.ratio() * 100)

            # 3. Analyze Fluency using heuristic
            # Since librosa is removed for deployment optimization, we approximate fluency
            # based on pronunciation score and transcription completeness
            if pron_score > 90:
                fluency_score = min(100, pron_score + 5)
            elif pron_score > 70:
                fluency_score = pron_score
            else:
                fluency_score = max(0, pron_score - 10)

            return {
                'pronunciation': pron_score,
                'fluency': min(100, fluency_score),
                'transcription': transcription,
                'status': 'success'
            }
        except Exception as e:
            print(f"Analysis Error: {e}")
            raise e
