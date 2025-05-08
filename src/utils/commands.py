from env import FILE_LOCATION
from datetime import datetime
from connections.Wiki import Wiki
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
        print("/start or /help command\n------")
        with open(f"{FILE_LOCATION}\\src\\utils\\files\\help.txt", "r", encoding="UTF-8") as f:
            await update.message.reply_text(f.read(), parse_mode=cts.ParseMode.HTML)

    @staticmethod
    async def hello_command(update, context):
        print("hello comand\n------")
        with open(f"{FILE_LOCATION}\\src\\utils\\files\\hello.txt", "r", encoding="UTF-8") as f:
            await update.message.reply_text(f.read(), parse_mode=cts.ParseMode.HTML)
    
    """
    Dictionary Handler
    """

    @staticmethod
    async def def_command(update, context):
        print("/def command\n")
        text = update.message.text.replace("/def", "")

        if not text:
            await update.message.reply_text("O comando /def deve ser usado como: <b>/def</b> <i>palavra</i>.",
                                            parse_mode=cts.ParseMode.HTML)
            return
        
        word = text.split()[0]
        
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

    """
    Wikipedia Handler
    """
     
    @staticmethod
    async def wiki_command(update, context):
        print("/wiki command\n------")
        argument = update.message.text
        argument = argument.replace("/wiki", "")

        if not argument:
            await update.message.reply_text("O comando /wiki deve ser usado como: <b>/wiki</b> <i>termo</i>.",
                                            parse_mode=cts.ParseMode.HTML)
        
        page = Wiki.get_page(argument)

        if page:
            message = f"<b>{argument.capitalize()}</b>, segundo a Wikipedia:\n\n" + f"<i>{page.summary}</i>"
            await update.message.reply_text(message, parse_mode=cts.ParseMode.HTML)
            return
        
        await update.message.reply_text("Não consegui achar uma página para isso...")

    """
    Handlers for Add and remove task Conversations
    """
    ASK_DATE, VALIDATE_ADD, VALIDATE_REMOVE = range(3)

    @staticmethod
    async def add_task_command(update, context):
        print("/addtask Command\n------")
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
        print("2.Processando data da tarefa\n------")     

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
        print("2. Processando data da tarefa\n------")     

        try:
            datetime.strptime(date, "%d/%m/%Y")
            DB.remove_task(update.message.chat.id, context.user_data["task_name"], date)

        except Exception as e:
            print(e)
            await update.message.reply_text("Não consegui deletar essa tarefa (Input inválido)")
            context.user_data.clear()

            return ConversationHandler.END

        print("Registro deletado com sucesso\n------")
        await update.message.reply_text("Tarefa removida com sucesso!")
        context.user_data.clear()
        return ConversationHandler.END

    @staticmethod
    async def seetasks_command(update, context):
        try:
            tasks = DB.get_tasks(update.message.chat.id)["tasks"]
        except Exception:
            return
        
        if not tasks:
            await update.message.reply_text("Você não possui tarefas salvas!!")
            return

        message = "Aqui estão suas tarefas:\n\n"

        for task in tasks:
            message += f"<i>{task["date"]}</i> - <b>{task["name"]}</b>\n"
        
        await update.message.reply_text(message, parse_mode=cts.ParseMode.HTML)


    """
    Handlers for Add and Remove test Conversation
    """

    ASK_TEST_DATE, VALIDATE_TEST_ADD, VALIDATE_TEST_REMOVE = range(3)

    @staticmethod
    async def add_test_command(update, context):
        print("/addtest Command\n------")
        context.user_data["test_operation"] = "add"

        if update.message.chat.type != "private":
            await update.message.reply_text("Esse comando só pode ser usado em chats privados!!")
            return

        await update.message.reply_text("Qual a sua prova?")
        return Commands.ASK_TEST_DATE 
    
    @staticmethod
    async def ask_test_date(update, context):
        name = update.message.text
        if not name:
            return Commands.conversation_cancel(update, context)
        
        print("1.Processando prova")

        context.user_data["test_name"] = name
        await update.message.reply_text("Qual a data da prova? (DD/MM/AAAA")

        if context.user_data["test_operation"] == "remove":
            return Commands.VALIDATE_TEST_REMOVE
        return Commands.VALIDATE_TEST_ADD
    
    @staticmethod
    async def validate_addtest(update, context):
        date = update.message.text
        print("2.Processando data da prova\n------")     

        try:
            datetime.strptime(date, "%d/%m/%Y")
            DB.add_test(update.message.chat.id, context.user_data["test_name"], date)
        except Exception as e:
            
            await update.message.reply_text("Não consegui adicionar essa prova (Input inválido)")
            context.user_data.clear()

            return ConversationHandler.END

        print("Registro com sucesso\n------")
        await update.message.reply_text("Prova Adicionada!")
        context.user_data.clear()

        return ConversationHandler.END
    
    @staticmethod
    async def remove_test_command(update, context):
        print("/removetest Command\n------")
        context.user_data["test_operation"] = "remove"

        if update.message.chat.type != "private":
            await update.message.reply_text("Esse comando só pode ser usado em chats privados!!")
            return

        await update.message.reply_text("Qual a sua prova?")
        return Commands.ASK_TEST_DATE 
    
    @staticmethod
    async def validate_removetest(update, context):
        date = update.message.text
        print("2. Processando data da prova\n------")     

        try:
            datetime.strptime(date, "%d/%m/%Y")
            DB.remove_test(update.message.chat.id, context.user_data["test_name"], date)

        except Exception as e:
            print(e)
            await update.message.reply_text("Não consegui deletar essa prova (Input inválido)")
            context.user_data.clear()

            return ConversationHandler.END

        print("Registro deletado com sucesso\n------")
        await update.message.reply_text("Prova removida com sucesso!")
        context.user_data.clear()
        return ConversationHandler.END
    
    @staticmethod
    async def seetests_command(update, context):
        try:
            tests = DB.get_tests(update.message.chat.id)["tests"]
        except Exception:
            return
        
        if not tests:
            await update.message.reply_text("Você não possui provas salvas!!")
            return

        message = "Aqui estão suas provas:\n\n"

        for test in tests:
            message += f"<i>{test["date"]}</i> - <b>{test["name"]}</b>\n"
        
        await update.message.reply_text(message, parse_mode=cts.ParseMode.HTML)
    
