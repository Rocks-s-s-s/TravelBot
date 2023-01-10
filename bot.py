"""
    TODO: 1. Исправить файл (tours.csv), хранящий описание туров.
             Добавить данные: страна, город, название тура, стоимость.
          2. В файле bot.py cоздать функцию main() для запуска бота и
             прописать обработку команды start для запуска бота.
             Использовать aiogram ver.3, вместо ver.2. (См. теоретический проект по Aiogram)
          3. Написать функцию, которая получает список всех типов отдыха (уникальных)
             (Использовать функцию чтения файла, которую написали в предыдущий раз)
"""
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'старт'])
async def process_start_command(message: types.Message):
    await message.answer("Вас приветствует Тревел бот. Я помогу вам найти тур для путишествия подходяший именно вам.")

if __name__ == '__main__':
    executor.start_polling(dp)
