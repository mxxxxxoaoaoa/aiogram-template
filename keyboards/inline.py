from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def generator_kb(items: int):
    markup = InlineKeyboardMarkup(row_width=7)
    for i in range(1, items):
        markup.insert(InlineKeyboardButton(str(i), callback_data="gen_{}".format(i)))
    return markup