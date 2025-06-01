import env

"""
Message handlers
"""

def message_processing(text : str) -> str | None:
    processed = text.lower()

    if "oi" in processed or "olá" in processed:
        return "Olá, tudo bem?"
    elif "obrigado" in processed:
        return "Denada!"
    
    return "Não consigo interpretar sua mensagem."


async def message_handler(update, context):
    type = update.message.chat.type
    text = update.message.text

    print(f"Update from {update.message.chat.id} in {type}: {text}\n------")

    if type == 'group' or type == 'supergroup':
        if env.BOT_USERNAME in text:
            response = message_processing(text)
        else:
            return
    else:
        response = message_processing(text)


    await update.message.reply_text(response)


async def error_message(update, context):
    print(f"Update: {update} -> Error: {context.error}\n------")