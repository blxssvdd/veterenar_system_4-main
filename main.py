from os import getenv
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.log.log import get_log
from app.routers.start import start_router
from app.routers.animals import animals_router
from app.routers.reviews import review_router

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()


# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router.include_routers(start_router, animals_router, review_router)


# Головна функція пакету
async def main() -> None:
    # Дістанемо токен бота з середовища
    TOKEN = getenv('7273541603:AAGFL6jXgHpgEdpUqfqLZwQJp4aBBOnMHeY')
    # Створимо об'єкт Bot
    bot = Bot("7273541603:AAGFL6jXgHpgEdpUqfqLZwQJp4aBBOnMHeY", default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)
    # Почнемо обробляти події для бота
    await dp.start_polling(bot)


# Точка входу
if __name__ == "__main__":
    asyncio.run(main())