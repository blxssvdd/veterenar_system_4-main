from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тваринок")
    builder.button(text="Додати тваринку на лікування")
    builder.button(text="Показати список вилікуваних тваринок")
    builder.button(text="Додати відгук")
    builder.button(text="Показати всі відгуки")
    builder.adjust(1)
    return builder.as_markup()