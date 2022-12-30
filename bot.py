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
