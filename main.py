from aiogram import executor
from aiogram.dispatcher.filters import Text
try:
    import asyncio
except ImportError:
    import trollius as asyncio
from config import dp
from my_addons.admin_command import start_command
from my_addons.scheduler import scheduler, schedule_command, notify
from my_addons.help_command import i_am_trying
from my_addons.myinfo_command import send_info
from my_addons.pictures_command import friend_picture
from my_addons.shop import shop_start
from my_addons.shop_adr import shop_adress
from my_addons.show_souvenier import show_souvenier
from my_addons.show_magnets import show_magnets
from my_addons.show_switshots import show_switshots
from my_addons.form_exe import (
    Form,
    cancel_handler,
    name_get,
    adress_get,
    get_age,
    age_check,
    day_check,
    process_done
)
from my_addons.kick_bot import (
    check_message,
    ban_user
)
from DB.database_for_bot import (
    init,
    create_table
)


async def startup(_):
    """
        запускаем дополнительные сторонние сервисы
    """
    init()
    create_table()
    asyncio.create_task(scheduler())





dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(i_am_trying, commands=['help'])
dp.register_message_handler(send_info, commands=['myinfo'])
dp.register_message_handler(friend_picture, commands=['picture'])
dp.register_callback_query_handler(shop_start, text='shop_start')
dp.register_callback_query_handler(shop_adress, text='shop_adress')
dp.register_message_handler(show_souvenier, Text(equals='Сувениры с Преисподни'))
dp.register_message_handler(show_switshots, Text(equals='Свитшоты с Преисподни'))
dp.register_message_handler(show_magnets, Text(equals='Магниты с Преисподни'))
dp.register_callback_query_handler(name_get, Text(startswith='buy_item '))
dp.register_message_handler(name_get, Text(equals='Нет'), state=Form.done)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
dp.register_message_handler(adress_get, state=Form.name)
dp.register_message_handler(get_age, state=Form.adress)
dp.register_message_handler(age_check, state=Form.age)
dp.register_message_handler(day_check, state=Form.day)
dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!')
dp.register_message_handler(schedule_command, Text(startswith="Напомнить "))
# dp.register_message_handler(notify, Text(startswith="Напомнить "))
dp.register_message_handler(check_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = startup)
