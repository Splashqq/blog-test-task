from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from tgbot.states import PostsStates


async def on_post_selected(
    c: CallbackQuery, button: Button, dialog_manager: DialogManager, post_id: int
):
    dialog_manager.dialog_data["post_id"] = post_id
    await dialog_manager.switch_to(PostsStates.post_detail)
