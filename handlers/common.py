from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: types.Message):
    await message.answer("Вас приветствует Тревел бот. \nЯ помогу вам найти тур для путишествия подходяший именно вам.")
