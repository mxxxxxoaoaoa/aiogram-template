from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from app import msgs

# this middleware change user language if is not in locales (optional)

class Middleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if message.from_user.language_code not in msgs['locales']:
            message.from_user.language_code = "en" # instead of "en" set your code