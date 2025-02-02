from telegram import Bot
import requests
import time
import os

# Carica configurazioni
TOKEN = os.getenv("TELEGRAM_TOKEN", "7708196939:AAFovtKbeoS7yQmAoT-DBcVoZdq97NpAp6Q")
CHAT_ID = os.getenv("CHAT_ID", "774265868")

bot = Bot(token=TOKEN)

def check_tokens():
    print("✅ Configurazione corretta!")
    print(f"Token: {TOKEN[:10]}...")
    print(f"Chat ID: {CHAT_ID}")

if __name__ == "__main__":
    try:
        check_tokens()
        print("🚀 Bot in esecuzione... (CTRL+C per fermare)")
        while True:
            # Esempio: invia un messaggio di prova
            bot.send_message(chat_id=CHAT_ID, text="🤖 Bot funzionante!")
            time.sleep(60)
    except Exception as e:
        print(f"❌ Errore: {str(e)}")
