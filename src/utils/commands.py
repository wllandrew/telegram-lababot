from main import BOT_USERNAME, BOT_NAME, TOKEN
import connections.dictionary as dic

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
    
    async def def_command(update, context):
        text = update.message.text
        word = text.split()[1]
        data = dic.Dictionary.get_definitions(word)

        resp = f"Estas são as definições para {word}"
        for n in data.split('\n'):
            resp += n + "\n"
        
        await update.message.reply_text(resp)
        