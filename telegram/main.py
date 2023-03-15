

from aiogram import Bot, Dispatcher
from aiogram import types, executor

from telegram import keyboard

# Initialization bot and dispatcher
Token = "5715816748:AAFT4IZEL8eE0XSMvhJ_2gisX8CAA6ln260"
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start_handler(msg: types.Message):
    await msg.answer("Добро пожаловать! Ниже кнопки возможностей, нажми на них", reply_markup=keyboard.main_keyboard)




if __name__ == '__main__':
    executor.start_polling(dp)
