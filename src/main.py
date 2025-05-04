import env
from utils.commands import Commands
from utils.messages import Message
from telegram.ext import Application, CommandHandler, MessageHandler, filters


def main():
    """
    Entry Point da aplicação
    """
    app = Application.builder().token(env.TOKEN).build()

    app.add_handler(CommandHandler("hello", Commands.hello_command))
    app.add_handler(CommandHandler("start", Commands.start_command))
    app.add_handler(CommandHandler("def", Commands.def_command))

    app.add_handler(MessageHandler(filters.TEXT, Message.message_handler))
    
    print("Bot inicializado.")
    app.run_polling()

if __name__ == "__main__":
    main()

