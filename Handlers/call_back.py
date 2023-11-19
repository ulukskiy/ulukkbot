import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from Database.sql_commands import Database
from Keyboards.inline_buttons import questionnaire_keyboard


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Manty or Plov!?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R like manty!"
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R like plov!"
    )


async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hello admin"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="hi simple guy"
        )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "manty")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "plov")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)