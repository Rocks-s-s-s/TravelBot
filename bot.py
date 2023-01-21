"""
    TODO: 1. Написать функцию get_country_by_type(type) для получения списка стран,
             в которых есть отдых необходимого типа
          2. Написать функцию get_tours(type, country) для получения туров с соответствующими параметрами.
          3. Необходимо написать функцию travel_type_keyboard(), которая генерирует клавиатуру
             с типами отдыха и выводит на экран для выбора пользователем.
"""
import asyncio
from aiogram import Bot, types,Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import common
import tours_context
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup


def travel_type_keyboard():
    pass

async def main():
    #создаём бота
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(common.router)
    filename = 'tours.csv'
    #получаем список типов туров
    types = tours_context.get_types_rest(filename)
    #создаём отдельные кнопки под каждый тип тура
    for type in types:
        buttonType = KeyboardButton(type)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(buttonType)

    await bot.set_my_commands([BotCommand(command='start', description='Старт')])
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
