from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from tgbot.getters import get_post_data, get_posts_data
from tgbot.handlers import on_post_selected
from tgbot.states import PostsStates

posts_dialog = Dialog(
    Window(
        Const("Список постов:"),
        ScrollingGroup(
            Select(
                Format("{item.title}"),
                id="s_posts",
                item_id_getter=lambda item: str(item.id),
                items="posts",
                on_click=on_post_selected,
            ),
            id="posts_scrolling",
            width=1,
            height=5,
        ),
        state=PostsStates.post_list,
        getter=get_posts_data,
    ),
    Window(
        Format("<b>{title}</b>\n\n{content}\n\n<i>Дата: {date}</i>"),
        Back(Const("Назад")),
        state=PostsStates.post_detail,
        getter=get_post_data,
        parse_mode="HTML",
    ),
)
