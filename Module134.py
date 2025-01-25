from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
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

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для расчета нормы калорий. Введите 'Calories', чтобы начать.")

@dp.message(lambda message: message.text == 'Calories')
async def set_age(message: types.Message, state: FSMContext):
    await message.reply('Введите свой возраст:')
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Возраст должен быть числом. Попробуйте снова.")
        return

    await state.update_data(age=int(message.text))
    await message.reply('Введите свой рост (в см):')
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Рост должен быть числом. Попробуйте снова.")
        return

    await state.update_data(growth=int(message.text))
    await message.reply('Введите свой вес (в кг):')
    await state.set_state(UserState.weight)

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

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())