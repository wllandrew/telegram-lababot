import env
from utils.Commands import Commands
from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, filters

class Conversations:
    
    ASK_DATE, VALIDATE_ADD, VALIDATE_REMOVE = range(3)

    addtask_conversation = ConversationHandler(
            entry_points=[CommandHandler("addtask", Commands.add_task_command)],
            states={
                    ASK_DATE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_taskdate)],
                    VALIDATE_ADD : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.validate_addtask)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )
    
    removetask_conversation = ConversationHandler(
            entry_points=[CommandHandler("removetask", Commands.remove_task_command)],
            states={
                    ASK_DATE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_taskdate)],
                    VALIDATE_REMOVE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.validate_removetask)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )