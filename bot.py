import logging
from aiogram import Bot, Dispatcher, types, executor

TOKEN = "6184887950:AAFfWE9Ugym8OmLDEd8I9qP45ekm_5k0Td8"

logging.basicConfig(level=logging.INFO)
proxy_url = 'http://proxy.server:3128' #для pythonanywhere

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.message):
	await message.answer(message.text)

if __name__ == "__main__":
	executor.start_polling(dp)
