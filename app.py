import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def process_terabox_link(input_string):
    logger.info(f"Processing Terabox link: {input_string}")
    s_index = input_string.find("/s/")
    if s_index == -1:
        return "Input is not terabox link"
    sliced_part = input_string[s_index + 3:]
    result = "https://teradownloader.com/download?link=https%3A%2F%2Fteraboxlink.com%2Fs%2F" + sliced_part
    return result

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("User started the bot")
    await update.message.reply_text('Welcome! Send me a TeraBox link, and I will process it for you.  seur')

async def process_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Processing user's link")
    terabox_link = update.message.text
    try:
        processed_link = process_terabox_link(terabox_link)
        await update.message.reply_text(f"Processed link: {processed_link}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    application = ApplicationBuilder().token("7851206013:AAHjswozTjh418zRjtLtc6otdeLmn2v6C_M" ).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("link", process_link))
    application.add_handler(MessageHandler(filters.Regex(r"/s/"), process_link))


    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
