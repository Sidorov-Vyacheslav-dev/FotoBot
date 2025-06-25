from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message, admin_ids) -> bool:
        print(message.from_user.id)
        return message.from_user.id in admin_ids

class IsFolder(BaseFilter):
    def __init__(self, folders_name: list[str]) -> None:
        self.folders_name = folders_name
    async def __call__(self, message: Message) -> bool:
        return message.text in self.folders_name