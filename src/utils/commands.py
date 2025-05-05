import re
from connections.exceptions.DatabaseException import DatabaseException
from connections.Database import DB
import connections.Dictionary as dic
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
        await update.message.reply_text("Qual o nome da sua tarefa?: ")
        return 0 # Redireciona para ask_task_name no conversation_handler
    
    @staticmethod
    async def ask_task_name(update, context):
        name = update.message.text
        if not name:
            return Commands.conversation_cancel(update, context)

        context.user_data["task_name"] = name
        await update.message.reply_text("Qual a data para entrega? (DD/MM)")

        return 1 # Redireciona para ask_task_date no conversation_handler
    
    @staticmethod
    async def ask_task_date(update, context):
        date = update.message.text
        if not re.search("\d{1,2}\/\d{1,2}\/\d{2,4}", date):
            return Commands.conversation_cancel(update, context)
        
        ## Implement date validation
        try:
            DB.add_task(update.message.chat.id, context.user_data["task_name"], date)
        except DatabaseException as e:
            print(e.message)

        return ConversationHandler.END
    
    @staticmethod
    async def conversation_cancel(update, context):
        context.user_data.clear()
        await update.message.reply_text("Não consegui realizar essa operação...")
        return ConversationHandler.END
    
    @staticmethod
    async def seetasks_command(update, context):
        tasks = DB.get_tasks(update.message.chat.id)

        message = "Aqui estão suas tarefas: "

        for task in tasks:
            message += f"{task["date"]} - {task["name"]}"
        
        await update.message.reply_text(message)