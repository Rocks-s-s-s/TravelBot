"""
    TODO: 1. Создать файл (tours.csv), хранящий описание туров.
             Каждый тур находится в отдельной строке.
             Данные разделены запятыми.
          2. В файле bot.py cоздать функцию main() для запуска бота и
             прописать обработку команды start для запуска бота.
          3. В отдельном файле (tours_context.py) создать функцию, которая
             читает данные из файла в двумерный массив, который содержит все данные
             о турах. Каждый тур в своём подмассиве, каждое значение хранится отдельным значением массива.
             Пример результата:
             [[номер тура, 'название тура', 'тип отдыха', ...прочие пункты... ], ... ]
"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'старт', 'cnfhn'])
async def process_start_command(message: types.Message):
    await message.answer("Вас приветствует Тревел бот. Я помогу вам найти тур для путишествия подходяший именно вам.")

if __name__ == '__main__':
    executor.start_polling(dp)
