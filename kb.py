from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="message me", callback_data="my_page")],
    [InlineKeyboardButton(text="any function", callback_data="menu")]
])

help = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="menu", callback_data="help")]
])
