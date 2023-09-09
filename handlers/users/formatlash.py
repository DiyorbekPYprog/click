from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command("format"))
async def bot_start(message: types.Message):
    text = "<i>Salom</i> \n"
    text+="<b>QALIN</b> \n"
    text+="<del> Chizish</del> \n"
    text+="<em>EMPHASIZED</em> \n"
    text+="<strong>VERY WELL</strong> \n"
    # text+="<small>VERY WELL</small> \n"
    text+="<ins>VERY WELL</ins> \n"
    # text+="LIFE<sub>VERY WELL</sub> \n"
    # text+="LIFE<sup>VERY WELL</sup> \n"
    # text+="<mark>VERY WELL</mark> \n"
    await message.answer(text)
