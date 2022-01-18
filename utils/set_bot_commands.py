from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("go_obed", "Создать опрос 'Го? Не го?'"),
            types.BotCommand("popular_poll", "Создать опрос с популярными местами"),
            types.BotCommand("add_option", "Создать опрос с популярными местами и добавить одно дополнительное"),
            types.BotCommand("get_menus", "Посмотреть менюшки"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )
