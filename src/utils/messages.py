from main import BOT_USERNAME, BOT_NAME, TOKEN

class Message:
    """
    Message handlers
    """

    @staticmethod
    def message_processing(text : str) -> str | None:
        processed = text.lower()

        if "oi" in processed or "olá" in processed:
            return "Olá, tudo bem?"
        
        return "Não consigo interpretar sua mensagem."

    @staticmethod
    async def message_handler(update, context):
        type = update.message.chat.type
        text = update.message.text

        if type == 'group' or type == 'supergroup':
            if BOT_USERNAME in text:
                response = Message.message_processing(text)
            else:
                return
        else:
            response = Message.message_processing(text)

        await update.message.reply_text(response)
