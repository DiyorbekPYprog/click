from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from keyboards.default.button import ichkiMenyu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=ichkiMenyu)

@dp.message_handler(IsPrivate(),text="salom")
async def bot_echo(message: types.Message):
    await message.answer("qalaysan")
    
@dp.message_handler(IsPrivate(),state=None)
async def bot_echo(message: types.Message):
    await message.answer("Sen lichkada yozayapsan")

