from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="message me", url='https://t.me/chorselty')],
    [InlineKeyboardButton(text="any function", callback_data="menu")]
])

help = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="menu", callback_data="help")]
])
