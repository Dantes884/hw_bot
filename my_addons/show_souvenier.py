from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def show_souvenier(message: types.Message):
    """
        Функция покажет сувениры
    """
    await message.answer(text='Вот сувениры:')
    await message.answer(text='Статуэтка Люцифера, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Балванчик в форме Сатаны, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Плакат с суккубами, стоимость - 1 душа', reply_markup=buy_item_kb)