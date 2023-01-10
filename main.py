from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from random import choice


load_dotenv()


bot = Bot(os.getenv('My_Token'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Здравствуй, смертный\n'
                        'Моё имя Астарот, я - высший демон!')
    await message.delete()


@dp.message_handler(commands=['help'])
async def i_am_trying(message: types.Message):
    await message.answer(text=f'/start - Я представлюсь как следует, чтобы тебе раз и навсегда стало ясно, кто перед тобой!\n'
                        f'/help - Ты прямо сейчас на нёё нажал...\n'
                        f'/myinfo - Я расскажу про тебя!\n'
                        f'/picture - Отправлю тебе фотографии своих друзей с Преисподни')
    await message.delete()


@dp.message_handler(commands=['myinfo'])
async def send_info(message: types.Message):
    await message.answer(text=f'Я всё о тебе знаю\n'
                        f'Твой id: {message.from_user.id}\n'
                        f'Твоё имя: {message.from_user.first_name}\n'
                        f'Твой ник: {message.from_user.username}.')
    await message.delete()


@dp.message_handler(commands=['picture'])
async def friend_picture(message: types.Message):
    photo = open('images/' + choice(os.listdir('images')), 'rb')
    await bot.send_photo(message.chat.id, photo)
    await message.delete()


@dp.message_handler()
async def chsv(message: types.Message):
    if len(message.text.split()) >= 3:
        await message.reply(text=message.text.upper())
    else:
        await message.answer(text='У меня нет желания отвечать тебе. Так что на беседу не надейся')


if __name__ == '__main__':
    executor.start_polling(dp)