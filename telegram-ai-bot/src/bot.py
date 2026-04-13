import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
from llm import get_llm_response

# Загружаем переменные окружения
load_dotenv()

# Настройки
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Не найден TELEGRAM_BOT_TOKEN в .env файле!")

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я AI-бот.\n"
        "Задай мне любой вопрос, и я постараюсь ответить!\n\n"
        "Команды:\n"
        "/start - Начать заново\n"
        "/help - Помощь"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📖 Помощь:\n\n"
        "Я использую языковую модель (LLM) для ответов на вопросы.\n"
        "Просто напиши мне сообщение, и я отвечу!\n\n"
        "⚡ Работает через OpenRouter API"
    )

# Обработчик текстовых сообщений
@dp.message()
async def handle_text(message: Message):
    # Показываем, что бот печатает
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    try:
        # Получаем ответ от LLM
        user_message = message.text
        logging.info(f"Пользователь {message.from_user.id}: {user_message}")
        
        response = await get_llm_response(user_message)
        
        # Отправляем ответ (разбиваем на части если длинный)
        if len(response) > 4096:
            for i in range(0, len(response), 4096):
                await message.answer(response[i:i+4096])
        else:
            await message.answer(response)
            
        logging.info(f"Ответ отправлен пользователю {message.from_user.id}")
        
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("😕 Извините, произошла ошибка. Попробуйте позже.")

# Главная функция
async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
