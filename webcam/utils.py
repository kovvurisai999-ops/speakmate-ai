import os
# Heavy imports moved inside classes to prevent startup crashes

class EmotionAnalyzer:
    def analyze_frame(self, frame):
        import cv2
        from deepface import DeepFace
        import numpy as np
        try:
            # DeepFace.analyze returns a list of results
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            if results:
                # Get the primary emotion and its score
                emotions = results[0]['emotion']
                dominant_emotion = results[0]['dominant_emotion']
                
                # We care about confidence/nervousness
                # Happy/Neutral -> High Confidence
                # Fear/Sad/Anxious -> Low Confidence
                
                confidence_score = emotions.get('happy', 0) + emotions.get('neutral', 0)
                nervousness_score = emotions.get('fear', 0) + emotions.get('sad', 0)
                
                return {
                    'dominant': dominant_emotion,
                    'confidence': confidence_score,
                    'nervousness': nervousness_score,
                    'all_emotions': emotions
                }
        except Exception as e:
            print(f"Emotion analysis error: {e}")
            return None
        return None

    def analyze_image_path(self, image_path):
        import cv2
        img = cv2.imread(image_path)
        if img is not None:
            return self.analyze_frame(img)
        return None
