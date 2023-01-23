from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import DB.database_for_bot


class Form(StatesGroup):
    name = State()
    adress = State()
    age = State()
    day = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.set_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply(
        'Отменено.',
        reply_markup=types.ReplyKeyboardRemove())


async def name_get(message: types.Message):
    """
    Узнаем имя
    """
    await Form.name.set()
    await message.reply("Введите ваше имя:")


async def adress_get(message: types.Message, state: FSMContext):
    """
    Обрабатываем имя, узнаем адресс
    """
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await Form.next()
    await message.reply("Введите ваш адресс:")


async def get_age(message: types.Message, state: FSMContext):
    """
    Обрабатываем адресс, узнаем возвраст
    """
    async with state.proxy() as data:
        data['adress'] = message.text
        print(data)

    await Form.next()
    await message.reply("Введите ваш возраст:")


async def age_check(message: types.Message, state: FSMContext):
    """
    Обрабатывваем возраст, задаем следующий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Введите возвраст числами")
    elif int(message.text) <= 18:
        await message.reply("Подождите достижения совершенолетия :)")
        await state.finish()
        await message.answer(
            'Будем ждать вас.',
            reply_markup=types.ReplyKeyboardRemove())
    else:
        async with state.proxy() as data:
            data['age']=int(message.text)

        week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        week_days_kb.add(
            KeyboardButton("Вторник"),
            KeyboardButton("Среда"),
            KeyboardButton("Четверг"),
            KeyboardButton("Пятница"),
            KeyboardButton("Суббота"),
            KeyboardButton("Воскресение"),
        )
        await Form.next()
        await message.reply(
            "Выберите день недели для получения посылки в ближайшую неделю",
            reply_markup=week_days_kb
        )


async def day_check(message: types.Message, state: FSMContext):
    """
    Обрабатываем введенный день недели, уточняем данные
    """
    async with state.proxy() as data:
        data['day']=message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.reply(f"""Подтвердите ваши данные:
    Имя: {data['name']}
    Возраст: {data['age']}
    Адрес: {data['adress']}
    День, когда вы можете получить посылку: {data['day']}
    Данные верны?
    """, reply_markup=yes_no_kb)

async def process_done(message: types.Message, state: FSMContext):
    """
    Сохраняем данные
    """
    await state.finish()
    await message.reply(
        "Спасибо. Я запомнил.",
        reply_markup=ReplyKeyboardRemove()
    )