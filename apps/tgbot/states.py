from aiogram.fsm.state import State, StatesGroup


class PostsStates(StatesGroup):
    post_list = State()
    post_detail = State()
