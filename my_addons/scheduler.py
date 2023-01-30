import asyncio
import aioschedule
from aiogram import types
from config import bot


async def schedule_command(message: types.Message):
    """
    Хендлер для того, чтбы получить команду от юзера и сохранить его id
    """
    global chat_id, remember
    chat_id = message.from_user.id
    remember = message.text.lower().replace('напомнить ', '')
    await message.answer(
        text="Хорошо"
    )


async def notify():
    """
    напоминалка
    """
    bot.send_message(
        chat_id=chat_id,
        text=remember
    )


async def scheduler():
    """
    Для того, чтобы по расписанию выполнять напоминалку
    """
    aioschedule.every(5).seconds.do(notify)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)