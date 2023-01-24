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
    demon_switshot = get_products()[6]
    switshot_hell_overcomplete = get_products()[7]
    switshot_when_i_come = get_products()[8]
    await message.answer_photo(
        open(demon_switshot[3], 'rb'),
        caption=f'{demon_switshot[1]}, стоимость - {demon_switshot[2]}',
        reply_markup=buy_item_kb(demon_switshot[0])
    )
    await message.answer_photo(
        open(switshot_hell_overcomplete[3], 'rb'),
        caption=f'{switshot_hell_overcomplete[1]}, стоимость - {switshot_hell_overcomplete[2]}',
        reply_markup=buy_item_kb(switshot_hell_overcomplete[0])
    )
    await message.answer_photo(
        open(switshot_when_i_come[3], 'rb'),
        caption=f'{switshot_when_i_come[1]}, стоимость - {switshot_when_i_come[2]}',
        reply_markup=buy_item_kb(switshot_when_i_come[0])
    )
    # await message.answer_photo(
    #     open('assortiments/49_3-800x800.jpg', 'rb'),
    #     caption="Свитшот демон, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/images.jfif', 'rb'),
    #     caption='Свитшот "Ад перевыполнен", стоимость - 1 душа',
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/62228_Svitshot_Kogda_ya_popadu_v_ad_.jpg', 'rb'),
    #     caption='Свитшот "Когда я попаду в ад", стоимость - 1 душа',
    #     reply_markup=buy_item_kb
    # )