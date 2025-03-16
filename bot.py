from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7896143767:AAEFIl0uDnmgkeGzTJ548pEo5rtxS7p8KKI"

# Start Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your bot. Send me a message!")

# Reply to Messages
async def echo(update: Update, context: CallbackContext):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")

# Main Function
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()