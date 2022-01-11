from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/go_obed - Создать опрос 'Го? Не го?'",
            "/popular_poll - Создать опрос с популярными местами",
            "/add_option - Создать опрос с популярными местами и добавть одно дополнительное",
            "/get_menus - Посмотреть менюшки",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))

