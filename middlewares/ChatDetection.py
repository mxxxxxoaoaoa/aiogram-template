from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from app import msgs
from keyboards import inline
from aiogram.dispatcher.handler import CancelHandler, current_handler

class Middleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if message.from_user.id == message.chat.id:
            # for answer to message:
            # await message.reply(msgs[message.from_user.language_code]['chat_detect'])
            raise CancelHandler()