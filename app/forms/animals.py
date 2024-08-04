from aiogram.fsm.state import State, StatesGroup


class AnimalForm(StatesGroup):
    name = State()