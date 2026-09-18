import random

fish = [
    {
        "nome": "Sardinha",
        "value": 10,
        "rarity": "Comun"
    },
    {
        "nome": "Atum",
        "value": 30,
        "rarity": "Incomum"
    },
    {
        "nome": "Tubarão",
        "value": 100,
        "rarity": "Raro"
    },
    {
        "nome": "Peixe Lendário",
        "value": 500,
        "rarity": "Lendário"
    }
]

def catch_fish(equipment):
    if equipment == "Vara Básica":
        weight = [70, 20, 8, 2]

    elif equipment == "Vara Média":
        weight = [60, 25, 10, 5]

    elif equipment == "Vara Profissional":
        weight = [50, 25, 15, 10]

    return random.choices(
        fish,
        weights = weight,
        k = 1
    )[0]



#catch = catch_fish()
# print(catch)