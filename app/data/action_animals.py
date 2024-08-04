import json

from app.data import list_files, open_files


def remove_animal(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринку '{animal}' успішно видалено."
    return msg


def healed_animals(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    healed_animals = open_files.get_healed_animals()
    healed_animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.HEALED_ANIMALS, "w", encoding="utf-8") as file:
        json.dump(healed_animals, file)

    msg = f"Тваринка '{animal}' успішно вилікувана. Дякую за використання нашої клініки."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тваринка '{animal}' вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринка '{animal}' успішно додана на лікування."
    return msg