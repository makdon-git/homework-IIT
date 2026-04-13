import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройки OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-exp:free")

# Клиент OpenAI (совместим с OpenRouter)
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

async def get_llm_response(user_message: str) -> str:
    """
    Отправляет запрос к LLM и возвращает ответ.
    
    Args:
        user_message: Сообщение от пользователя
        
    Returns:
        Ответ от языковой модели
    """
    try:
        response = await client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Ты полезный ассистент. Отвечай кратко и по делу."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Ошибка при получении ответа: {str(e)}"
