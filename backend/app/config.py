import os


class Config:
    # ===== GOOGLE GEMINI CONFIG =====
    GOOGLE_GEMINI_API_KEY = os.environ.get('GOOGLE_GEMINI_API_KEY') or None
