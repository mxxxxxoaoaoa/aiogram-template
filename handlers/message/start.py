from aiogram import types, Dispatcher
import asyncio
from data import messages


async def func(message: types.Message):
    return await message.answer(
        msgs[message.from_user.language_code]['start_message']
    )


async def wrapper(message: types.Message):
    await asyncio.create_task(func(message))


def register(dp: Dispatcher):
    dp.register_message_handler(wrapper, commands=['start'])
