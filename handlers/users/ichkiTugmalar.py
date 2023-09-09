from aiogram import types
from keyboards.inline.ichkitugma import ClickPremnium
from keyboards.inline.ichkitugma import Utkazmalar

from loader import dp


@dp.message_handler(text="👑 Click Premium")
async def bot_start(message: types.Message):
    await message.answer("👑 Click Premium",reply_markup=ClickPremnium)

@dp.message_handler(text="🔀 O'tkazmalar")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Utkazmalar)