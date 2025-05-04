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
    
    @staticmethod
    async def def_command(update, context):
        text = update.message.text
        word = text.split()[1]
        data = dic.Dictionary.get_definitions(word)

        if not data:
            await update.message.reply_text(f"Não consigo achar a definição para {word}!!")
            return

        resp = f"Estas são as definições para {word}:\n"
        definitions = data.split("\n")
        for i in range(len(definitions)):
            resp += f"{i} - {definitions[i]}\n"
        
        await update.message.reply_text(resp)
        