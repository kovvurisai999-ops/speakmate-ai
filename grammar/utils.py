import os
from ai_engine.gemini import gemini_ai
from dotenv import load_dotenv

load_dotenv()

class GrammarChecker:
    def __init__(self):
        # We now use the centralized gemini_ai engine
        self.ai = gemini_ai

    def check(self, text):
        if not text: return None, "Please speak something.", False
        
        # 0. Telugu/Multilingual Detection (Very basic check to avoid false spelling errors)
        # If the text contains common Telugu phonetics but is written in English script, we skip basic spelling
        telugu_hints = ['andi', 'ela', 'unnaru', 'nenu', 'enti', 'avunu', 'kadu', 'bagundi']
        is_multilingual = any(hint in text.lower() for hint in telugu_hints)

        # 1. Use Gemini AI if enabled (Premium Dynamic Analysis)
        if self.ai.enabled:
            try:
                system_prompt = (
                    "You are an English Grammar Expert. Analyze the user's sentence. "
                    "If it has errors, provide the correct version and a short explanation. "
                    "If it is correct OR if it is a mix of English and Telugu (like 'hi andi'), respond with 'PERFECT'. "
                    "Format: [Corrected Sentence] | [Short Explanation]"
                )
                result = self.ai.ask(system_prompt, text, max_tokens=100)
                
                if "PERFECT" in result.upper():
                    return None, "Excellent! Your sentence is perfectly structured.", True
                
                if "|" in result:
                    parts = result.split("|")
                    corrected = parts[0].strip()
                    explanation = parts[1].strip()
                    return corrected, f"Suggested: {corrected}. {explanation}", False
                
                return result, f"AI Suggestion: {result}", False
                
            except Exception as e:
                print(f"Gemini Grammar Error: {e}")

        # 2. Local Heuristic Fallback (For offline or limit issues)
        lower_text = text.lower().strip()
        words = lower_text.split()
        if len(words) >= 2:
            first, second = words[0], words[1]
            if first in ['i', 'you', 'we', 'they']:
                if second == 'goes': return text.replace(words[1], "go"), "Grammar: Use 'I go' instead of 'I goes'.", False
            if first in ['he', 'she', 'it']:
                if not second.endswith('s') and second not in ['can', 'will', 'must', 'may', 'should', 'did', 'had', 'went']:
                    return text, f"Grammar: '{first.capitalize()}' needs a verb with 's'. Did you mean '{second}s'?", False

        # 3. Spelling Fallback (Skipped for multilingual hints)
        if not is_multilingual:
            try:
                from textblob import TextBlob
                blob = TextBlob(text)
                corrected = str(blob.correct())
                def clean(t): return "".join(c for c in t.lower() if c.isalnum() or c.isspace()).strip()
                if clean(corrected) != clean(lower_text):
                    return corrected, f"Spelling issue: Suggested '{corrected}'.", False
            except ImportError:
                pass  # textblob not available, skip spelling check

        return None, "Excellent! Your sentence is perfectly structured.", True
