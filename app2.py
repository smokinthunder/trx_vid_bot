import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# RapidAPI credentials
RAPIDAPI_KEY = "452e0ac1f5mshfc0ab50beeb55e0p15b98djsn687513ed817b"
RAPIDAPI_HOST = "terabox-downloader-direct-download-link-generator.p.rapidapi.com"

def get_video_link(url):
    payload = {"url": url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"https://{RAPIDAPI_HOST}/fetch", json=payload, headers=headers)
    data = response.json()[0]['dlink']
    return data

def start(update, context):
    update.message.reply_text('Hello! Send me a Terabox video link.')

def handle_message(update, context):
    try:
        chat_id = update.effective_chat.id
        terabox_link = update.message.text
        
        if terabox_link.startswith("/s/"):
            video_link = get_video_link(terabox_link)
            update.message.reply_text(video_link)
        else:
            update.message.reply_text("Invalid Terabox link. Please send a link starting with '/s/'")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    TOKEN = "7851206013:AAHjswozTjh418zRjtLtc6otdeLmn2v6C_M"  # Replace with your actual bot token
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
