from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('Сувениры с Преисподни'),
    KeyboardButton('Свитшоты с Преисподни'),
    KeyboardButton('Магниты с Преисподни')
)


async def shop_start(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки магазин
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Что тебя интересует?',
        reply_markup=shop_kb
    )