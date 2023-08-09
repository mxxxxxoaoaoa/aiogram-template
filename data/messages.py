# en locale

start_msg_en = """
🥺 beat me, humiliate me, please, I want to be your slave\.
"""
generate_msg_en = """
🤠 u generated kb for {} buttons\.

😮 click on them\!\! 
"""

generate_msg_error_en = """
🤕 u dont enter number
example: /generate *6*
"""

gen_answer_en = """
😶‍🌫️ its {} number\.
"""

# uk locale

start_msg_uk = """
🥺 бийте мене, принижуйте мене, будь ласка, я хочу бути вашим рабом\.
"""
generate_msg_uk = """
🤠 ти згенерував клавіатуру на {} кнопки\.

😮 тисни на них\!\! 
"""

generate_msg_error_uk = """
🤕 ти не вказав число
наприклад: /generate *6*
"""

gen_answer_uk = """
😶‍🌫️ це {}\.
"""

# ru locale

start_msg_ru = """
🥺 бей меня, унижай меня, пожалуйста, я хочу быть твоим рабом\.
"""
generate_msg_ru = """
🤠 ты сгенерировал клавиатуру на {} кнопок\.

😮 нажми на них\!\! 
"""

generate_msg_error_ru = """
🤕 ты не ввел число
например: /generate *6*
"""

gen_answer_ru = """
😶‍🌫️ это {}\.
"""

data = {
    "locales": ['ru', 'en', 'uk'],
    "en": {},
    "uk": {},
    "ru": {}
}


data['en'] = {
    "start_message": start_msg_en,
    "generate_msg": generate_msg_en,
    "generate_error": generate_msg_error_en,
    "generate_answer": gen_answer_en,
}

data['uk'] = {
    "start_message": start_msg_uk,
    "generate_msg": generate_msg_uk,
    "generate_error": generate_msg_error_uk,
    "generate_answer": gen_answer_uk,
}

data['ru'] = {
    "start_message": start_msg_ru,
    "generate_msg": generate_msg_ru,
    "generate_error": generate_msg_error_ru,
    "generate_answer": gen_answer_ru,
}


def load_messages():
    return data