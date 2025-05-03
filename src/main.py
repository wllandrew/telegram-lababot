import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
BOT_USERNAME = os.getenv("BOT_USERNAME")

"""
MESSAGE HANDLERS
"""
def message_processing(text : str) -> str | None:
    processed = text.lower()

    if "oi" in processed or "olá" in processed:
        return "Olá, tudo bem?"
    
    return "Não consigo interpretar sua mensagem."

async def message_handler(update, context):
    type = update.message.chat.type
    text = update.message.text

    if type == 'group' or type == 'supergroup':
        if BOT_USERNAME in text:
            response = message_processing(text)
        else:
            return
    else:
        response = message_processing(text)

    await update.message.reply_text(response)

"""
COMMAND HANDLERS
"""
async def start_command(update, context):
    print("Star command")
    await update.message.reply_text("Eu sou o LabaBot, um bot que te ajuda a estudar.\nMeus comandos atuais são:\n/hello")

async def hello_command(update, context):
    print("Hello comand")
    await update.message.reply_text("Olá, eu sou o Lababot.")


def main():
    """
    Entry Point da aplicação
    """
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello_command))
    app.add_handler(CommandHandler("start", start_command))

    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    print("Bot inicializado.")
    app.run_polling()

if __name__ == "__main__":
    main()

