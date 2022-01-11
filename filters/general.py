import aiogram.types
from aiogram.dispatcher.filters import BoundFilter
from data import config


class IsAdmin(BoundFilter):
    async def check(self, message: aiogram.types.Message):
        return str(message.from_user.id) in config.ADMINS
