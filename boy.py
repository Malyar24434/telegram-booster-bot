TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN tak jumpa! Pastikan set kat Render Environment Variables")
