import os
import utils.commands as commands
import utils.messages as messages
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
BOT_USERNAME = os.getenv("BOT_USERNAME")

def main():
    """
    Entry Point da aplicação
    """
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", commands.hello_command))
    app.add_handler(CommandHandler("start", commands.start_command))

    app.add_handler(MessageHandler(filters.TEXT, messages.message_handler))
    print("Bot inicializado.")
    app.run_polling()

if __name__ == "__main__":
    main()

