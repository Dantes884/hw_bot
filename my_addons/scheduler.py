import asyncio
import aioschedule
from aiogram import types
from config import bot


async def schedule_command(message: types.Message):
    """
    Хендлер для того, чтбы получить команду от юзера и сохранить его id
    """
    global chat_id
    chat_id = message.from_user.id
    await message.answer(
        text="Хорошо"
    )
    remind_text = message.text.replace('Напомнить ', '')


async def notify(message: types.Message):
    """
    напоминалка
    """
    await bot.send_message(
        chat_id=chat_id,
        text=message.text.replace('Напомнить ', '')
    )


async def scheduler():
    """
    Для того, чтобы по расписанию выполнять напоминалку
    """
    aioschedule.every(5).seconds.do(notify)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

