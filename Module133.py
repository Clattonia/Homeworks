from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties  
import asyncio


api = ''


bot = Bot(
    token=api,
    default=DefaultBotProperties(parse_mode="HTML")  
)


dp = Dispatcher(storage=MemoryStorage())


@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот. Как дела?")

@dp.message()  
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    