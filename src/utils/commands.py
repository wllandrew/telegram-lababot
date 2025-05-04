from main import BOT_USERNAME, BOT_NAME, TOKEN

class Commands:
    """
    Command Handlers
    """

    @staticmethod
    async def start_command(update, context):
        print("Star command")
        await update.message.reply_text("Eu sou o LabaBot, um bot que te ajuda a estudar.\nMeus comandos atuais são:\n/hello")

    @staticmethod
    async def hello_command(update, context):
        print("Hello comand")
        await update.message.reply_text("Olá, eu sou o Lababot.")