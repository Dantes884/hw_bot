from aiogram import types


async def shop_adress(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки адресса
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Мы находимя в Преисподни, слева от цитадели Сатаны',
    )