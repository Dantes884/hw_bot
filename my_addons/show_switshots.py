from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DB.database_for_bot import get_products

def buy_item_kb(product_id):
    buy_item_kb = InlineKeyboardMarkup()
    buy_item_kb.add(InlineKeyboardButton('Купить', callback_data=f'buy_item {product_id}'))
    return buy_item_kb


async def show_switshots(message: types.Message):
    """
        Функция покажет свитшоты
    """
    await message.answer(text='Вот свитшоты:')
    i = 6
    while i <= 8:
        variable = get_products()[i]
        await message.answer_photo(
            open(variable[3], 'rb'),
            caption=f'{variable[1]}, стоимость - {variable[2]}',
            reply_markup=buy_item_kb(variable[0])
        )
        i += 1