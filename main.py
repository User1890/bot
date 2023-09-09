from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import config, asyncio, text, kb
from commands_bot import set_commands
from handlers import router
import aiogram.utils.markdown as md

bot = Bot(token = config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.callback_query(F.data == 'help')
async def call_menu(msg: Message):
    await msg.answer()
    await bot.send_message(msg.from_user.id, text.menu, reply_markup=kb.menu)


@dp.callback_query(F.data == 'my_page')
async def call_menu(msg: Message):
    await msg.answer()
    await bot.send_photo(msg.from_user.id, photo='https://avatars.mds.yandex.net/get-images-cbir/4398029/6oLOkdh382QwiwLyrkHTNA4605/ocr', caption=md.hlink("Chorselty", "https://t.me/chorselty"))
    await bot.send_message(config.CHANEL_ID, text=text.chanel.format(name = msg.from_user.first_name, id = msg.from_user.id))


@dp.callback_query(F.data == 'menu')
async def call_menu(msg: Message):
    await msg.answer("f")


@dp.message(Command('h'))
async def menu(msg : Message):
    await msg.answer(text.help, reply_markup=kb.help)


@dp.message(Command("m"))
async def menu(msg : Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@dp.message(Command("start"))
async def get_start(msg : Message, bot : Bot):
    await bot.send_message(msg.from_user.id, text=text.greet.format(name = msg.from_user.first_name), reply_markup=kb.help)


async def main():

    await set_commands(bot)
    await dp.start_polling(bot, on_startup=set_commands)
    

if __name__ == "__main__":
    asyncio.run(main())