from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
ClickPremnium = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Oyiga 50'000 so'mga ulash",callback_data="m"),
    ],
    [
        InlineKeyboardButton(text="Oyiga 50'000 so'mga ulash",callback_data="n"),
    ]]
)
Utkazmalar = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="📲 Telefon raqam orqali",callback_data="a"),
    ],
    [
        InlineKeyboardButton(text="💳 Karta raqami orqali",callback_data="b"),
    ],
    [
        InlineKeyboardButton(text="💠 Click-Hamyonga o'tkazma",callback_data="c"),
    ],
    [
        InlineKeyboardButton(text=" 🔁 O'z kartalarim orasida",callback_data="d"),
    ],
    [
        InlineKeyboardButton(text="💭 Telegram chat orqali",callback_data="e"),
    ],
    [
        InlineKeyboardButton(text="QR-kod boyicha o'tkazma",callback_data="f"),
    ],
    [
        InlineKeyboardButton(text="Mening QR-kodim",callback_data="g"),
    ]]
)