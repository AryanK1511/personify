import os


class Config:
<<<<<<< HEAD
    # ===== GOOGLE GEMINI CONFIG =====
    GOOGLE_GEMINI_API_KEY = os.environ.get('GOOGLE_GEMINI_API_KEY') or None
=======
    pass
    # # ===== POSTGRESQL CONFIG =====
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or None

    # # ===== CLOUDINARY CONFIG =====
    # CLOUDINARY_CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME")
    # CLOUDINARY_API_KEY = os.environ.get("CLOUDINARY_API_KEY")
    # CLOUDINARY_API_SECRET = os.environ.get("CLOUDINARY_API_SECRET")

    # # ==== JWT SECRET ====
    # JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
>>>>>>> main
