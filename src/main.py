import env
from utils.Commands import Commands
from utils.Messages import Message
from utils.Conversations import Conversations
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler,filters


def main():
    """
    Entry Point da aplicação
    """
    app = Application.builder().token(env.TOKEN).build()

    app.add_handler(CommandHandler("hello", Commands.hello_command))
    app.add_handler(CommandHandler("start", Commands.start_command))
    app.add_handler(CommandHandler("def", Commands.def_command))
    app.add_handler(CommandHandler("seetasks", Commands.seetasks_command))
    app.add_handler(CommandHandler("seetests", Commands.seetests_command))
    app.add_handler(CommandHandler("wiki", Commands.wiki_command))

    app.add_handler(Conversations.addtask_conversation)
    app.add_handler(Conversations.removetask_conversation)
    app.add_handler(Conversations.addtest_conversation)
    app.add_handler(Conversations.removetest_conversation)


    app.add_handler(MessageHandler(filters.TEXT, Message.message_handler))
    
    app.add_error_handler(Message.error_message)
    
    print("Bot inicializado.\n-----")
    app.run_polling(poll_interval=2)

if __name__ == "__main__":
    main()

