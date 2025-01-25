from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
import asyncio

api = '6667937375:AAF7nMENkFRjF67VDxEcz8i0t6dfZvxmXgE'

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')]  
], resize_keyboard=True)


inline_kb_products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для расчета нормы калорий.", reply_markup=kb)


@dp.message(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    
    products = [
        {"name": "Product1", "description": "описание 1", "price": 100},
        {"name": "Product2", "description": "описание 2", "price": 200},
        {"name": "Product3", "description": "описание 3", "price": 300},
        {"name": "Product4", "description": "описание 4", "price": 400},
    ]

    for product in products:
        product_info = f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}"
        await message.answer(product_info)
        
        photo = types.FSInputFile("1.jpg")  
        await message.answer_photo(photo)

    
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb_products)


@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())