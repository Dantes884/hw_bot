from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DB.database_for_bot import get_products


def buy_item_kb(product_id):
    buy_item_kb = InlineKeyboardMarkup()
    buy_item_kb.add(InlineKeyboardButton('Купить', callback_data=f'buy_item {product_id}'))
    return buy_item_kb


async def show_souvenier(message: types.Message):
    """
        Функция покажет сувениры
    """
    await message.answer(text='Вот сувениры:')
    i = 3
    while i < 6:
        variable = get_products()[i]
        await message.answer_photo(
            open(variable[3], 'rb'),
            caption=f'{variable[1]}, стоимость - {variable[2]}',
            reply_markup=buy_item_kb(variable[0])
        )
        i += 1