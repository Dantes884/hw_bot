from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def show_magnets(message: types.Message):
    """
        Функция покажет магниты
    """
    await message.answer(text='Вот магниты:')
    await message.answer_photo(
        open('assortiments/magnit-gori-v-adu-s-bananovymi-listyami-scaled.jpg', 'rb'),
        caption="Магнит ада, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/neFCfKCmpH3SmoJX.png', 'rb'),
        caption="Магнит преисподни, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/n9HkP1gjZyE620yW4lyvkCF1ZIH9KtyfJNFWZwVt-1024x1024.jpeg', 'rb'),
        caption="Магнит бездны, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )