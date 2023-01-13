"""
    TODO: 1. Написать по подобию проекта Aiogram рабочий бот, который запускается. Всё дело в версии библиотеки.
             То, что тут написано другой версии, мы используем уже давно новую.
             Использовать aiogram ver.3, вместо ver.2. (См. теоретический проект по Aiogram)
          2. Написать функцию, которая получает список всех типов отдыха (уникальных)
             (Использовать функцию чтения файла, которую написали в предыдущий раз)
"""

from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def main():
    @dp.message_handler(commands=['start', 'старт'])
    async def process_start_command(message: types.Message):
        await message.answer("Вас приветствует Тревел бот. Я помогу вам найти тур для путишествия подходяший именно вам.")

if __name__ == '__main__':
    executor.start_polling(dp)
