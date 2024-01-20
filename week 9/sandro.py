from telegram import Update;
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

bot_token = "6753183278:AAGcL2CQSbOY9gzS_6rQyBh38PSmjE3BDe0"
bot_username = "Test1VersionBot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("boturi boti tkvens samsaxurshi simon, cade /help ")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("uechveli /custom naxe")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("bazari araa me viyo boti")


def handle_response(text: str):
    text = text.lower()
    if "hello" in text:
        return "Zdarova brat"
    return "azze ar var"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.chat.type
    text = update.message.text

    print(f"user {update.message.chat.id} in {message}: {text}")

    if message == "group":
        if bot_username in text:
            text = text.replace(bot_username, "").strip()
            response = handle_response(text)
        else:
            return
    else:
        response = handle_response(text)
    
    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update} {context.error}")

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)