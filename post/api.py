from typing import List

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError
from ninja.security import HttpBearer

from post.models import Post
from post.schemas import PostIn, PostOut


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


router = Router()


@router.post("/login", auth=None)
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user is not None:
        return {"token": "supersecret"}
    raise HttpError(401, "Invalid credentials")


@router.get("/posts", response=List[PostOut])
def list_posts(request):
    posts = Post.objects.all()
    return posts


@router.get("/posts/{post_id}", response=PostOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router.post("/posts", response=PostOut)
def create_post(request, payload: PostIn):
    post = Post.objects.create(**payload.dict())
    return post


@router.put("/posts/{post_id}", response=PostOut)
def update_post(request, post_id: int, payload: PostIn):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return post


@router.delete("/posts/{post_id}")
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {"success": True}
