from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def show_souvenier(message: types.Message):
    """
        Функция покажет сувениры
    """
    await message.answer(text='Вот сувениры:')
    await message.answer_photo(
        open('assortiments/2604061696_w700_h500_kollektsionnaya-statuetka-veronese.webp', 'rb'),
        caption="Статуэтка Люцифера, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/png-transparent-baphomet-wheel-sigil-of-baphomet-.png', 'rb'),
        caption="Колесо Бафомета, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/3910343172_w600_h600_3910343172.webp', 'rb'),
        caption="Плакат с суккубами, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )