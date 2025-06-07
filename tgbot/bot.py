import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from blog.settings import env
from tgbot.dialogs import posts_dialog
from tgbot.states import PostsStates

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Используйте /posts, чтобы увидеть список постов.")


@router.message(Command("posts"))
async def posts_command(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(PostsStates.post_list, mode=StartMode.RESET_STACK)


async def start_bot():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=env("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(posts_dialog)
    setup_dialogs(dp)

    await dp.start_polling(bot)
