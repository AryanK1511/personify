from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app import app

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
