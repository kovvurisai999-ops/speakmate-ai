class Translator:
    _instance = None
    _failed = False

    @classmethod
    def get_instance(cls):
        if cls._failed:
            return None
        if cls._instance is None:
            try:
                from transformers import MarianMTModel, MarianTokenizer
                model_name = "Helsinki-NLP/opus-mt-te-en"
                print("Loading translation model (this may take a moment)...")
                cls._tokenizer = MarianTokenizer.from_pretrained(model_name)
                cls._model = MarianMTModel.from_pretrained(model_name)
                cls._instance = cls()
            except Exception as e:
                print(f"Translation model loading failed: {e}. Switching to English-only mode.")
                cls._failed = True
                return None
        return cls._instance

    def translate(self, text):
        if not text: return ""
        # Simple check if text is Telugu (very basic)
        # In a real app, use langdetect
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        translated = self._model.generate(**inputs)
        return self._tokenizer.decode(translated[0], skip_special_tokens=True)
