from utils.Commands import Commands
from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, filters

class Conversations:
    
    """
    Task conversations
    """

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
    
    """
    Test conversations
    """
    ASK_TEST_DATE, VALIDATE_TEST_ADD, VALIDATE_TEST_REMOVE = range(3)

    addtest_conversation = ConversationHandler(
            entry_points=[CommandHandler("addtest", Commands.add_test_command)],
            states={
                    ASK_TEST_DATE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_test_date)],
                    VALIDATE_TEST_ADD : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.validate_addtest)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )
    
    removetest_conversation = ConversationHandler(
            entry_points=[CommandHandler("removetest", Commands.remove_test_command)],
            states={
                    ASK_TEST_DATE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_test_date)],
                    VALIDATE_TEST_REMOVE : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.validate_removetest)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )
    
    """
    Timer conversations.
    """
    ASK_POM_TIME, ASK_POM_ROUNDS, ASK_BREAK_TIME = range(3)

    pomodoro_conversation = ConversationHandler(
            entry_points=[CommandHandler("startpomodoro", Commands.start_pomodoro)],
            states={
                    ASK_POM_TIME : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_pomodoro_time)],
                    ASK_POM_ROUNDS : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_pom_round)],
                    ASK_BREAK_TIME : [MessageHandler(filters.TEXT & ~filters.COMMAND, Commands.ask_break_time)]
                },
            fallbacks=[CommandHandler("cancel", Commands.conversation_cancel)]
        )