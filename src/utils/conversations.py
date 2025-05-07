import env
from utils.Commands import Commands
from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, filters

class Conversations:
    
    ASK_NAME, ASK_DATE = range(2)

    addtask_conversation = ConversationHandler(
            entry_points=[CommandHandler("addtask", Commands.addtask_command)],
            states={
                    ASK_NAME : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_name_command)],
                    ASK_DATE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_date_command)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )