import random

fish = [
    {
        "nome": "Sardinha",
        "value": 10,
        "rarity": "Comum"
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

areas = {
    "Praia": {
        "level": 1,
        "fish": ["Sardinha", "Atum"]
    },

    "Mar aberto": {
        "level": 3,
        "fish": ["Atum", "Tubarão"]
    },

    "Ilha misteriosa": {
        "level": 8,
        "fish": ["Tubarão", "Peixe Lendário"]
    }
}

def catch_fish(equipment,area):

    avaliable_fish = [
        fish_item
        for fish_item in fish
        if fish_item["nome"] in areas[area]["fish"]
    ]

    if equipment == "Vara Básica":
        weight = [70, 30]

    elif equipment == "Vara Média":
        weight = [60, 40]

    elif equipment == "Vara Profissional":
        weight = [50, 50]

    return random.choices(
        avaliable_fish,
        weights = weight,
        k = 1
    )[0]



#catch = catch_fish()
# print(catch)