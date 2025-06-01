from datetime import date, datetime
from connections.Database import DB

"""
Handlers dos tests
"""

async def test_timer(context):
    job = context.job
    DB.remove_test(job.chat_id, job.name, job.data)
    await context.bot.send_message(job.chat_id, text=f"\U000026A0 Você tem uma prova hoje!!:\n{job.data}  -  {job.name}\n")


def set_test_timer(update, context):     
    test_date = datetime.strptime(context.user_data["test_date"], "%d/%m/%Y")

    if test_date.date() <= date.today():
        raise Exception("Invalid date")

    context.job_queue.run_once(test_timer, test_date, name=context.user_data["test_name"], chat_id=update.message.chat_id, data=context.user_data["test_date"])


def remove_jobs(name, context) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    
    if not current_jobs:
        return False
    
    for job in current_jobs:
        job.schedule_removal()
    return True

"""
Handlers do pomodoro
"""

async def round_timer(context):
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"\U0001F345 Vamos para o round {job.data}!")


async def break_timer(context):
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"\U0001F345 Vamos tirar uma pausa de {job.data} minutos.")


async def pomodoro_fim(context):
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"\U0001F345 Fim dessa sessão. Tire uma pausa maior e se distraia!")
    context.user_data["pomodoro"] = False


def set_pomodoro_job(update, context):

    context.job_queue.run_once(round_timer, 1, name="Pomodoro", chat_id=update.message.chat_id, data=1)

    if context.user_data["qtd_rounds"] == 1:
        return
    
    time_sum = context.user_data["round_time"]

    for rounds in range(1, context.user_data["qtd_rounds"]):
        if rounds != 0:
            context.job_queue.run_once(break_timer, time_sum * 60, name="Pomodoro", chat_id=update.message.chat_id, data=context.user_data["break_time"])
            time_sum += context.user_data["break_time"]
        
        context.job_queue.run_once(round_timer, time_sum * 60, name="Pomodoro", chat_id=update.message.chat_id, data=rounds+1)
        time_sum += context.user_data["round_time"]  

    context.job_queue.run_once(pomodoro_fim, time_sum * 60, name="Pomodoro", chat_id=update.message.chat_id, data=rounds+1)