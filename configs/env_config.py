from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env
load_dotenv()

# Чтение переменных
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Значение по умолчанию