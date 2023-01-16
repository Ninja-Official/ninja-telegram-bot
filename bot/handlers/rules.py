from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from bot import application
from bot.services.auto_delete import auto_delete

RULES_TEXT = (
    "Чат является важным средством коммуникации, но при чрезмерном использовании он "
    "может оказать негативное влияние на здоровье сообщества."
    "\n\n"
    "Т.к. группа в телеграме является частью сообщества Mirea Ninja, в "
    "ней действуют те же правила, что и на форуме, но с некоторыми поправками на эфемерность:"
    "\n\n"
    "1. 😈 Можно материться. Обзываться и переходить на личности - нельзя.\n"
    "2. 👺 Анонимность != вседозволенность. Мы <i>рекомендуем</i> не подрывать учебный процесс и не нарушать законы РФ,"
    " используя этот чат.\n"
    "3. 👋 С новыми участниками у нас принято общаться на «ты» и относиться к ним как к друзьям. Будьте вежливы.\n"
    "4. 🤝 Прося что-то, давайте что-то взамен. Если вам помогли, не забудьте поставить +реп.\n"
    "5. 🚪 Это частная вечеринка. Если вы очень душный — вас выставляют за дверь. Тут нет демократии."
)


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await update.effective_message.reply_html(
        RULES_TEXT,
    )
    auto_delete(message, context, from_message=update.effective_message)


# show chat rules
application.add_handler(CommandHandler("rules", rules))
