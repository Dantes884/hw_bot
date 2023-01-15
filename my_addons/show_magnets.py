from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy item'))


async def show_magnets(message: types.Message):
    """
        Функция покажет магниты
    """
    await message.answer(text='Вот магниты:')
    await message.answer(text='Магнит ада, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Магнит Бездны, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Магнит Преисподни, стоимость - 1 душа', reply_markup=buy_item_kb)