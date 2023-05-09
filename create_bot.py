from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
#create bot
TOKEN = ""
with open('token.txt') as file:
    TOKEN: str = file.readline()
proxy_url = 'http://proxy.server:3128'
bot = Bot(TOKEN)
dp = Dispatcher(bot)
