from aiogram import types, Dispatcher
import asyncio
from keyboards import inline
from app import msgs

async def func(message: types.Message):
    args = message.get_args()
    if args != "" and args.isdigit():
        print(args)
        kb = inline.generator_kb(int(args))
        return await message.answer(
            msgs[message.from_user.language_code]['generate_message'].format(args),
            reply_markup=kb
        )
    else:
        return await message.answer(msgs[message.from_user.language_code]['generate_error'])


async def wrapper(message: types.Message):
    await asyncio.create_task(func(message))


def register(dp: Dispatcher):
    dp.register_message_handler(wrapper, commands=['generate'])