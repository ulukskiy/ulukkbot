from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start PPPP",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 😎",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Manty",
        callback_data="manty"
    )
    mojo_button = InlineKeyboardButton(
        "Plov",
        callback_data="plov"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup