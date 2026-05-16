import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class GeminiEngine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeminiEngine, cls).__new__(cls)
            api_key = os.getenv("GEMINI_API_KEY")
            if api_key:
                try:
                    cls._instance.client = genai.Client(api_key=api_key)
                    cls._instance.model_name = "gemini-flash-latest"
                    cls._instance.enabled = True
                except Exception as e:
                    print(f"Gemini Init Error: {e}")
                    cls._instance.enabled = False
            else:
                cls._instance.enabled = False
        return cls._instance

    def ask(self, system_prompt, user_input, max_tokens=150):
        if not self.enabled:
            return "AI service is currently offline. Please check your API key."

        try:
            print(f"DEBUG: Gemini Ask - Input: {user_input[:50]}...")
            # Setting up config for economy mode
            config = types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=max_tokens,
                temperature=0.7,
            )
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=user_input,
                config=config
            )
            text = response.text.strip()
            print(f"DEBUG: Gemini Ask - Success")
            return text
        except Exception as e:
            print(f"ERROR: Gemini Ask Failed: {e}")
            return f"I'm having a bit of trouble thinking right now. (Error: {str(e)[:50]})"

# Global instance
gemini_ai = GeminiEngine()
