import env
from utils.Commands import Commands
from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, filters

class Conversations:
    
    addtask_conversation = ConversationHandler(
            entry_points=[CommandHandler("addtasks", Commands.addtask_command)],
            states={
                    0 : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_name)],
                    1 : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_date)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )