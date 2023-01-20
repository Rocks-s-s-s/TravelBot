"""
    TODO: 1. Написать функцию get_country_by_type(type) для получения списка стран,
             в которых есть отдых необходимого типа
          2. Написать функцию get_tours(type, country) для получения туров с соответствующими параметрами.
          3. Необходимо написать функцию travel_type_keyboard(), которая генерирует клавиатуру
             с типами отдыха и выводит на экран для выбора пользователем.
"""
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import common
import tours_context

def travel_type_keyboard():
    pass

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(common.router)
    await bot.set_my_commands([BotCommand(command='start', description='Старт')])
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
