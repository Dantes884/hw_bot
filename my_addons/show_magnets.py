from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DB.database_for_bot import get_products

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def show_magnets(message: types.Message):
    """
        Функция покажет магниты
    """
    await message.answer(text='Вот магниты:')
    magnet_hell = get_products()[0]
    magnet_underworld = get_products()[1]
    magnet_abyss = get_products()[2]
    await message.answer_photo(
        open(magnet_hell[3], 'rb'),
        caption=f'{magnet_hell[1]}, стоимость - {magnet_hell[2]}',
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open(magnet_underworld[3], 'rb'),
        caption=f'{magnet_underworld[1]}, стоимость - {magnet_underworld[2]}',
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open(magnet_abyss[3], 'rb'),
        caption=f'{magnet_abyss[1]}, стоимость - {magnet_abyss[2]}',
        reply_markup=buy_item_kb
    )


    # await message.answer_photo(open
    #     open('assortiments/magnit-gori-v-adu-s-bananovymi-listyami-scaled.jpg', 'rb'),
    #     caption="Магнит ада, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/neFCfKCmpH3SmoJX.png', 'rb'),
    #     caption="Магнит преисподни, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )
    # await message.answer_photo(
    #     open('assortiments/n9HkP1gjZyE620yW4lyvkCF1ZIH9KtyfJNFWZwVt-1024x1024.jpeg', 'rb'),
    #     caption="Магнит бездны, стоимость - 1 душа",
    #     reply_markup=buy_item_kb
    # )