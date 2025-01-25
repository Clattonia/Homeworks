from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '6667937375:AAF7nMENkFRjF67VDxEcz8i0t6dfZvxmXgE'

bot = Bot(
    token=api,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher(storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обычная клавиатура
kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')]
], resize_keyboard=True)

# Inline-клавиатура
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для расчета нормы калорий.", reply_markup=kb)

# Обработчик кнопки 'Рассчитать'
@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

# Обработчик Inline-кнопки 'Формулы расчёта'
@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n"
        "Для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) - 161"
    )
    await call.message.answer(formula_text)
    await call.answer()

# Обработчик Inline-кнопки 'Рассчитать норму калорий'
@dp.callback_query(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)
    await call.answer()

# Обработчик состояния age
@dp.message(UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Возраст должен быть числом. Попробуйте снова.")
        return

    await state.update_data(age=int(message.text))
    await message.reply('Введите свой рост (в см):')
    await state.set_state(UserState.growth)

# Обработчик состояния growth
@dp.message(UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Рост должен быть числом. Попробуйте снова.")
        return

    await state.update_data(growth=int(message.text))
    await message.reply('Введите свой вес (в кг):')
    await state.set_state(UserState.weight)

# Обработчик состояния weight
@dp.message(UserState.weight)
async def process_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Вес должен быть числом. Попробуйте снова.")
        return

    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories:.2f} ккал/день.")
    await state.finish()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())