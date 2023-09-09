from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import config, asyncio, text, kb
from commands_bot import set_commands


bot = Bot(token = config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == '/h')
async def menu(msg : Message):
    await msg.answer(text.help, reply_markup=kb.help)


@dp.callback_query(F.data == 'help')
async def call_menu(msg: Message):
    await bot.send_message(msg.from_user.id, text.menu, reply_markup=kb.menu)


@dp.message(F.text == '/m')
async def menu(msg : Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@dp.callback_query(F.data == 'menu')
async def call_menu(msg: Message):
    await msg.edit_reply_markup(msg.message_id, reply_markup=kb.help)
    await msg.__setstate__


@dp.callback_query()
async def cal_menu(msg: Message):
    await bot.send_message(config.CHANEL_ID, text=text.chanel.format(name = msg.from_user.first_name, id = msg.from_user.id))

@dp.message(F.text == '/start')
async def get_start(msg : Message, bot : Bot):
    await bot.send_message(msg.from_user.id, text=text.greet.format(name = msg.from_user.first_name), reply_markup=kb.help)


async def main():
    await set_commands(bot)
    await dp.start_polling(bot, on_startup=set_commands)

if __name__ == "__main__":
    asyncio.run(main())