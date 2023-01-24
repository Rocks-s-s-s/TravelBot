"""
    TODO: 1. Необходимо написать функцию travel_type_keyboard(), которая генерирует клавиатуру
             с типами отдыха и выводит на экран для выбора пользователем.
             Клавиатура появляется после приветствия бота.
          2. Необходимо написать функцию country_keyboard(type), которая генерирует клавиатуру
             с доступными по типу странами.
"""
import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import common
import tours_context
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup


async def main():
    #создаём бота
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(common.router)

    # -------------- Тут не должно этого быть --------------
    filename = 'tours.csv'
    #получаем список типов туров
    types = tours_context.get_types_rest(filename)
    #создаём отдельные кнопки под каждый тип тура
    for type in types:
        buttonType = KeyboardButton(type)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(buttonType)
    # -------------- ------------------------ --------------

    await bot.set_my_commands([BotCommand(command='start', description='Старт')])
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
