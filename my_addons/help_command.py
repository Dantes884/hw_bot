from aiogram import types

from my_addons.constants import HELP_TEXT


async def i_am_trying(message: types.Message):
    """
        Функция покажет пользователю команды
    """
    await message.answer(text=HELP_TEXT)
    await message.delete()