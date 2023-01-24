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
    lucifer = get_products()[3]
    bafomet_wheel = get_products()[4]
    succub_poster = get_products()[5]
    await message.answer_photo(
        open(lucifer[3], 'rb'),
        caption=f'{lucifer[1]}, стоимость - {lucifer[2]}',
        reply_markup=buy_item_kb(lucifer[0])
    )
    await message.answer_photo(
        open(bafomet_wheel[3], 'rb'),
        caption=f'{bafomet_wheel[1]}, стоимость - {bafomet_wheel[2]}',
        reply_markup=buy_item_kb(bafomet_wheel[0])
    )
    await message.answer_photo(
        open(succub_poster[3], 'rb'),
        caption=f'{succub_poster[1]}, стоимость - {succub_poster[2]}',
        reply_markup=buy_item_kb(succub_poster[0])
    )
    # await message.answer_photo(
    #     open('assortiments/2604061696_w700_h500_kollektsionnaya-statuetka-veronese.webp', 'rb'),
    #     caption="Статуэтка Люцифера, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/png-transparent-baphomet-wheel-sigil-of-baphomet-.png', 'rb'),
    #     caption="Колесо Бафомета, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/3910343172_w600_h600_3910343172.webp', 'rb'),
    #     caption="Плакат с суккубами, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )