# Базовый образ Python
FROM python:3.11-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY src/ ./src/

# Переменные окружения по умолчанию
ENV TELEGRAM_BOT_TOKEN=""
ENV OPENROUTER_API_KEY=""
ENV OPENROUTER_MODEL="google/gemini-2.0-flash-exp:free"

# Команда запуска
CMD ["python", "src/bot.py"]
