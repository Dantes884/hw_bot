import asyncio

from aiogram import executor
from aiogram.dispatcher.filters import Text

from config import dp
from DB.database_for_bot import create_table, init
from my_addons.admin_command import start_command
from my_addons.form_exe import (Form, adress_get, age_check, cancel_handler,
                                day_check, get_age, name_get, process_done)
from my_addons.help_command import i_am_trying
from my_addons.kick_bot import ban_user, check_message
from my_addons.myinfo_command import send_info
from my_addons.pictures_command import friend_picture
from my_addons.scheduler import schedule_command, scheduler
from my_addons.shop import shop_start
from my_addons.shop_adr import shop_adress
from my_addons.show_magnets import show_magnets
from my_addons.show_souvenier import show_souvenier
from my_addons.show_switshots import show_switshots


async def startup(_):
    """
        запускаем дополнительные сторонние сервисы
    """
    init()
    create_table()
    asyncio.create_task(scheduler())

#Регистрирую команду старт
dp.register_message_handler(start_command, commands=['start'])
#Регистрирую команду, которая выведет все команды
dp.register_message_handler(i_am_trying, commands=['help'])
#Регистрирую команду для выведения информации про пользователя
dp.register_message_handler(send_info, commands=['myinfo'])
#Регистрирую команду для отправки случайного картинки
dp.register_message_handler(friend_picture, commands=['picture'])
#Регистрирую первый отклик на inline keyboard button и вывожу keyboard button с товарами
dp.register_callback_query_handler(shop_start, text='shop_start')
#Регистрирую второй отклик на inline keyboard button, про адресс магазина
dp.register_callback_query_handler(shop_adress, text='shop_adress')
#Регистрирую отклики на keyboard button с товарами
dp.register_message_handler(show_souvenier, Text(equals='Сувениры с Преисподни'))
dp.register_message_handler(show_switshots, Text(equals='Свитшоты с Преисподни'))
dp.register_message_handler(show_magnets, Text(equals='Магниты с Преисподни'))
#Регистрирую отклик на кнопку купить, вывожу анкету для заполнения
dp.register_callback_query_handler(name_get, Text(startswith='buy_item '))
#Сохраняю ответы пользователя
dp.register_message_handler(adress_get, state=Form.name)
dp.register_message_handler(get_age, state=Form.adress)
dp.register_message_handler(age_check, state=Form.age)
dp.register_message_handler(day_check, state=Form.day)
#Заношу данные пользователя, в случае правильного заполнения анкеты, в БД
dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
#Отменяю неправильно-заполненную анкету и не сохраняю её в БД
dp.register_message_handler(name_get, Text(equals='Нет'), state=Form.done)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
#Регистрирую напоминалку
#СКОЛЬКО НЕРВНЫХ Я ПОТРАТИЛ НА ЭТУ &$&#&, я его и так делал и сяк, уже пытался через apschedule!
#А ОКАЗЫВАЕТСЯ ВСЁ ДЕЛО БЫЛО В ВЕРСИИ ПИТОНА?!?!?!? Я усталь.
dp.register_message_handler(schedule_command, Text(startswith="Напомнить "))
#Регистрирую команду бана пользователя в групповом чате при помощи команды
dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!')
#Проверяю сообщения в групповом чате, на наличии плохих слов
dp.register_message_handler(check_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)