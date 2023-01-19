from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def show_switshots(message: types.Message):
    """
        Функция покажет свитшоты
    """
    await message.answer(text='Вот свитшоты:')
    await message.answer_photo(
        open('assortiments/49_3-800x800.jpg', 'rb'),
        caption="Свитшот демон, стоимость - 1 душа",
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/images.jfif', 'rb'),
        caption='Свитшот "Ад перевыполнен", стоимость - 1 душа',
        reply_markup=buy_item_kb
    )
    await message.answer_photo(
        open('assortiments/62228_Svitshot_Kogda_ya_popadu_v_ad_.jpg', 'rb'),
        caption='Свитшот "Когда я попаду в ад", стоимость - 1 душа',
        reply_markup=buy_item_kb
    )