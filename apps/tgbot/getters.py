import logging

from aiogram_dialog import DialogManager
from asgiref.sync import sync_to_async

from apps.post.models import Post


def get_all_posts():
    return list(Post.objects.all().order_by("-created_at"))


async def get_posts_data(**kwargs):
    posts = await sync_to_async(get_all_posts)()
    logging.debug(posts)
    return {"posts": posts}


async def get_post_data(dialog_manager: DialogManager, **kwargs):
    post_id = dialog_manager.dialog_data.get("post_id")
    post = await sync_to_async(Post.objects.get)(id=post_id)
    return {
        "title": post.title,
        "content": post.content,
        "date": post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    }
