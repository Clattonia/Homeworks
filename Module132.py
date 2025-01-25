from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command  
import asyncio


api = '6667937375:AAF7nMENkFRjF67VDxEcz8i0t6dfZvxmXgE'


bot = Bot(
    token=api,
    default=DefaultBotProperties(parse_mode="HTML")  
)


dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start")) 
async def send_welcome(message: types.Message):
    print("Привет! Я бот. Как дела?")


@dp.message()  
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())