from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from crud_functions145 import initiate_db, get_all_products, add_user, is_included

api = '6667937375:AAF7nMENkFRjF67VDxEcz8i0t6dfZvxmXgE'

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


initiate_db()


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')],
    [KeyboardButton(text='Регистрация')]  
], resize_keyboard=True)


inline_kb_products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для расчета нормы калорий.", reply_markup=kb)

@dp.message(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        product_info = f"Название: {title} | Описание: {description} | Цена: {price}"
        await message.answer(product_info)
        photo = FSInputFile("1.jpg")
        await message.answer_photo(photo)
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb_products)


@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message(lambda message: message.text == 'Регистрация')
async def sign_up(message: types.Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом. Попробуйте снова.")
        return

    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = int(age)

    
    add_user(username, email, age)
    await message.answer(f"Регистрация завершена! Добро пожаловать, {username}.")
    await state.finish()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())