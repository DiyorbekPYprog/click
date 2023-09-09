from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.button import ichkiMenyu
from keyboards.default.inbut import innbut
from keyboards.default.sozlamalar import settingbut
from loader import dp



@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=ichkiMenyu)

@dp.message_handler(text="💸 To'lov")
async def bot_hand(message: types.Message):
    await message.answer("To'lov turini tanlang",reply_markup=innbut)

@dp.message_handler(text="🔙 Asosiy menyuga qaytish")
async def asosiymenyu(message: types.Message):
    await message.answer("Asosiy menyu",reply_markup=ichkiMenyu)

@dp.message_handler(text="⚙️ Sozlamalar")
async def sozlamamenyu(message: types.Message):
    await message.answer("Sozlamalar",reply_markup=settingbut)

