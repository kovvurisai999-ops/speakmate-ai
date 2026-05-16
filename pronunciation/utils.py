import os
import librosa
import numpy as np
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

            # 3. Analyze Fluency using Librosa
            speech, sample_rate = librosa.load(audio_path, sr=16000)
            intervals = librosa.effects.split(speech, top_db=30)
            
            duration = len(speech) / sample_rate
            speech_time = sum([(end - start) for start, end in intervals]) / sample_rate
            
            num_pauses = max(0, len(intervals) - 1)
            fluency_score = int((speech_time / duration) * 100) if duration > 0 else 0
            
            if num_pauses > 3:
                fluency_score = max(0, fluency_score - (num_pauses * 5))

            return {
                'pronunciation': pron_score,
                'fluency': min(100, fluency_score),
                'transcription': transcription,
                'status': 'success'
            }
        except Exception as e:
            print(f"Analysis Error: {e}")
            raise e
