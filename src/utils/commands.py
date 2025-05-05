from connections.database import DB
import connections.dictionary as dic
from telegram.ext import ConversationHandler

class Commands:
    """
    Command Handlers
    """

    @staticmethod
    async def start_command(update, context):
        print("Star command\n------")
        await update.message.reply_text("Eu sou o LabaBot, um bot que te ajuda a estudar.\nMeus comandos atuais são:\n/hello")

    @staticmethod
    async def hello_command(update, context):
        print("Hello comand\n------")
        await update.message.reply_text("Olá, eu sou o Lababot.")
    
    @staticmethod
    async def def_command(update, context):
        print("Def command\n")
        text = update.message.text
        word = text.split()[1]
        data = dic.Dictionary.get_definitions(word)

        if not data:
            print(f"Não achou a definição para {word}.\n------")
            await update.message.reply_text(f"Não consigo achar a definição para {word}!!")
            return

        print("Status OK\n------")

        message = f"Aqui estão as definições para {word}:\n"

        count = 1
        for definition in data:
            for line in definition.split('\n'):
                if not line:
                    continue
                message += f"{count} - {line}\n".replace('_', '')
                count += 1
        
        await update.message.reply_text(message)
        

    @staticmethod
    async def addtask_command(update, context):
        
        return 0 # Redireciona para ask_task_name no conversation_handler
    
    @staticmethod
    async def ask_task_name(update, contextn):
        return 1 # Redireciona para ask_task_date no conversation_handler
    
    @staticmethod
    async def ask_task_date(update, context):
        return ConversationHandler.END
    
    @staticmethod
    async def conversation_cancel(update, context):
        await update.message.reply_text("Não consegui realizar essa operação...")
        return ConversationHandler.END
    
    @staticmethod
    async def seetasks_command(update, context):
        pass