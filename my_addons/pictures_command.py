from os import listdir
from random import choice

from aiogram import Bot, types


async def friend_picture(message: types.Message):
    """
        Функция выберет картинку из папки и отправит её пользователю
    """
    photo = open('images/' + choice(listdir('images')), 'rb')
    await message.answer_photo(photo)
    await message.delete()
