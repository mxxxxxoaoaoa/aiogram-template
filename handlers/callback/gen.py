from aiogram import types, Dispatcher
import asyncio
from app import msgs
import app

async def func(cq: types.CallbackQuery):
    num = cq.data.split("_")[-1]
    await app.bot.answer_callback_query(cq.id)
    await cq.message.answer(
        msgs[message.from_user.language_code]['generate_answer'].format(num)
    )


async def wrapper(cq: types.CallbackQuery):
    await asyncio.create_task(func(cq))


def register(dp: Dispatcher):
    dp.register_callback_query_handler(wrapper, lambda call: call.data.startswith("gen_"))
    # dp.register_message_handler(wrapper, lambda call: call.data == "") ## strictly equals
    # dp.register_message_handler(wrapper, lambda call: call.data in ['', '', ''])
