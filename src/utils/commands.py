from datetime import datetime
from connections.Database import DB
import connections.Dictionary as dic
from telegram.ext import ConversationHandler
from telegram import constants as cts

class Commands:
    """
    Command Handlers
    """

    @staticmethod
    async def start_command(update, context):
        print("/start command\n------")
        await update.message.reply_text("Eu sou o LabaBot, um bot que te ajuda a estudar.\nUse <bd>/</b> para ver meus comandos.",
                                        parse_mode=cts.ParseMode.HTML)

    @staticmethod
    async def hello_command(update, context):
        print("/hello comand\n------")
        await update.message.reply_text("Olá, eu sou o <b>Lababot</b>, um bot criado por <i>wllandrew @ github</i>, como posso te ajudar?",
                                        parse_mode=cts.ParseMode.HTML)
    
    @staticmethod
    async def def_command(update, context):
        print("/def command\n")
        text = update.message.text
        word = text.split()[1]
        data = dic.Dictionary.get_definitions(word)

        if not data:
            print(f"Não achou a definição para {word}.\n------")
            await update.message.reply_text(f"Não consigo achar a definição para {word}!!")
            return

        print("Status OK\n------")

        message = f"Aqui estão as definições para <b>{word}</b>:\n\n<i>"

        count = 1
        for definition in data:
            for line in definition.split('\n'):
                if not line:
                    continue
                message += f"{count} - {line}\n".replace('_', '')
                count += 1
        
        await update.message.reply_text(f"{message}</i>", parse_mode=cts.ParseMode.HTML)
        

    ASK_DATE, VALIDATE_ADD, VALIDATE_REMOVE = range(3)

    @staticmethod
    async def add_task_command(update, context):
        print("/addtask Command")
        context.user_data["task_operation"] = "add"

        if update.message.chat.type != "private":
            await update.message.reply_text("Esse comando só pode ser usado em chats privados!!")
            return

        await update.message.reply_text("Qual o nome da sua tarefa?")
        return Commands.ASK_DATE 
    
    @staticmethod
    async def ask_taskdate(update, context):
        name = update.message.text
        if not name:
            return Commands.conversation_cancel(update, context)
        
        print("1.Processando nome da tarefa")

        context.user_data["task_name"] = name
        await update.message.reply_text("Qual a data para entrega? (DD/MM/AAAA")

        if context.user_data["task_operation"] == "remove":
            return Commands.VALIDATE_REMOVE
        return Commands.VALIDATE_ADD # Redireciona para ask_task_date no conversation_handler
    
    @staticmethod
    async def validate_addtask(update, context):
        date = update.message.text
        print("2.Processando data da tarefa")     

        try:
            datetime.strptime(date, "%d/%m/%Y")
            DB.add_task(update.message.chat.id, context.user_data["task_name"], date)
        except Exception as e:
            
            await update.message.reply_text("Não consegui adicionar essa tarefa (Input inválido)")
            context.user_data.clear()

            return ConversationHandler.END

        print("Registro com sucesso\n------")
        await update.message.reply_text("Tarefa Adicionada!")
        context.user_data.clear()

        return ConversationHandler.END
    
    @staticmethod
    async def conversation_cancel(update, context):
        context.user_data.clear()
        print("Cancelamento")

        await update.message.reply_text("Não consegui realizar essa operação...")
        return ConversationHandler.END
    
    @staticmethod
    async def remove_task_command(update, context):
        print("1. Processando nome da tarefa")
        context.user_data["task_operation"] = "remove"

        if update.message.chat.type != "private":
            await update.message.reply_text("Esse comando só pode ser usado em chats privados!!")
            return

        await update.message.reply_text("Qual o nome da sua tarefa?")
        return Commands.ASK_DATE 
    
    @staticmethod
    async def validate_removetask(update, context):
        date = update.message.text
        print("2. Processando data da tarefa")     

        try:
            datetime.strptime(date, "%d/%m/%Y")
            DB.remove_task(update.message.chat.id, context.user_data["task_name"], date)

        except Exception as e:
            print(e)
            await update.message.reply_text("Não consegui deletar essa tarefa (Input inválido)")
            context.user_data.clear()

            return ConversationHandler.END

        print("Registro deletado com sucesso")
        await update.message.reply_text("Tarefa removida com sucesso!")
        context.user_data.clear()
        return ConversationHandler.END

    @staticmethod
    async def seetasks_command(update, context):
        try:
            tasks = DB.get_tasks(update.message.chat.id)["tasks"]
        except Exception:
            await update.message.reply_text("Você não possui tarefas salvas!!")
            return

        message = "Aqui estão suas tarefas:\n\n"

        for task in tasks:
            message += f"<i>{task["date"]}</i> - <b>{task["name"]}</b>\n"
        
        await update.message.reply_text(message, parse_mode=cts.ParseMode.HTML)