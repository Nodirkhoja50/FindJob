from django.core.management.base import BaseCommand
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher,Bot,executor,types
from .buttons import button,keyboard
from .keep import save_user,send_result
from ...models import UserBot
import os
from dotenv import dotenv_values,load_dotenv
load_dotenv()


API_TOKEN=os.getenv("TOKEN")



class Command(BaseCommand):
    def handle(self, *args,**options):

        bot = Bot(token=API_TOKEN)
        dp = Dispatcher(bot)
        languages = ['Python','C++','Java','JavaScript','HTML','CSS','SQL','C','TypeSript','Bash/Shell','Go','Swift']

        @dp.message_handler(commands=['start', 'help'])
        async def send_welcome(message: types.Message):

            await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup =button)
            print(message.from_user.id)



        @dp.message_handler(Text(startswith='ish beruvchi'))
        async def echo(message: types.Message):

            await message.answer('iltimos shu link orqali formani tolidiring, http://127.0.0.1:8000/form/')

        @dp.message_handler(Text(startswith='ishchi'))
        async def echo(message: types.Message):

            await message.reply("Hi,Please choose:",reply_markup = keyboard)


        @dp.callback_query_handler(text = languages)
        async def callback_query_handler(call: types.CallbackQuery):
           save_user(call.from_user.id,call.data)

           
           for i in send_result(call.data):
               send_link = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton
                    (
                        text ='Watch',url=f'http://127.0.0.1:8000/detail/{i["id"]}'
                        )
                        )
               await call.message.answer(f'*{i["scope"]}*\nCompany:{i["company_name"]}\nSteck:{i["main_language"]}\nBase money:${i["base_salary"]}\nLocation:{i["location"]}',parse_mode="Markdown",reply_markup=send_link)
        executor.start_polling(dp, skip_updates=True)
            
        executor.start_polling(dp, skip_updates=True)



a=Command()

a.handle()


