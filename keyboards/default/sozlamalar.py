from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

settingbut = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔙 Asosiy menyuga qaytish')
    ],
    [
        KeyboardButton(text="🔐 CLICK-PIN bilan tasdiqlash"),
        KeyboardButton(text="👭 Mening do'stlarim")
    ],
    [
        KeyboardButton(text="🔔 Xabarnomalar"),
        KeyboardButton(text="🌍 Tilni o'zgartirish")
    ],
    [
        KeyboardButton(text="📘 Foydalanuvchi uchun qo'llanma"),
        KeyboardButton(text="➖ Ma'lumotlarni o'chirish")
    ],
    [KeyboardButton(text='🔙 Asosiy menyuga qaytish')
    ]
    ],)