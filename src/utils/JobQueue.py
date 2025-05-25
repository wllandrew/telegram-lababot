from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import date, datetime
from connections.Database import DB

class JobHandler:
    
    """
    Handlers primários dos tests
    """

    @staticmethod
    async def test_timer(context):
        job = context.job
        DB.remove_task(job.chat_id, job.name, job.data)
        await context.bot.send_message(job.chat_id, text=f"A sua prova de {job.name} é hoje!!")

    @staticmethod
    def set_test_timer(update, context):     
        test_date = datetime.strptime(context.user_data["test_date"], "%d/%m/%Y")

        if test_date.date() < date.today():
            raise Exception("Invalid date")
        
        context.job_queue.run_once(JobHandler.test_timer, test_date, name=context.user_data["test_name"], chat_id=update.message.chat_id, data=context.user_data["test_date"])
    
    @staticmethod
    def remove_jobs(name, context) -> bool:
        current_jobs = context.job_queue.get_jobs_by_name(name)
        
        if not current_jobs:
            return False
        
        for job in current_jobs:
            job.schedule_removal()
        return True
    