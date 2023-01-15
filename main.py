from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging
from my_addons.admin_command import start_command
from my_addons.help_command import i_am_trying
from my_addons.myinfo_command import send_info
from my_addons.pictures_command import friend_picture
from my_addons.shop import shop_start
from my_addons.shop_adr import shop_adress
from my_addons.show_souvenier import show_souvenier
from my_addons.show_magnets import show_magnets
from my_addons.show_switshots import show_switshots
from my_addons.buy_item import buy_item
from my_addons.echo_command import chsv

load_dotenv()
bot = Bot(getenv('MY_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(i_am_trying, commands=['help'])
dp.register_message_handler(send_info, commands=['myinfo'])
dp.register_message_handler(friend_picture, commands=['picture'])
dp.register_callback_query_handler(shop_start, text='shop_start')
dp.register_callback_query_handler(shop_adress, text='shop_adress')
dp.register_message_handler(show_souvenier, Text(equals='Сувениры с Преисподни'))
dp.register_message_handler(show_switshots, Text(equals='Свитшоты с Преисподни'))
dp.register_message_handler(show_magnets, Text(equals='Магниты с Преисподни'))
dp.register_callback_query_handler(buy_item, text='buy_item')
dp.register_message_handler(chsv)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)