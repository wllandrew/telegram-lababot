import env
from commands import Commands
from telegram.ext import ConversationHandler, CommandHandler, filters

class Conversations:
    
    addtask_conversation = ConversationHandler(
            entry_points=[CommandHandler("start", Commands.addtask_command)],
            states={
                    0 : CommandHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_name),
                    1 : CommandHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_task_date)
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )