import random

fish = [
    {
        "nome": "Robalo",
        "value": 3,
        "rarity": "Comum"
    },
    {
        "nome": "Sardinha",
        "value": 5,
        "rarity": "Comum"
    },
    {
        "nome": "Anchova",
        "value": 8,
        "rarity": "Comum"
    },
    {
        "nome": "Cavala",
        "value": 10,
        "rarity": "Incomum"
    },
    {
        "nome": "Pargo",
        "value": 12,
        "rarity": "Incomum"
    },

    {
        "nome": "Corvina",
        "value": 15,
        "rarity": "Comum"
    },
    {
        "nome": "Tainha",
        "value": 18,
        "rarity": "Comum"
    },
    {
        "nome": "Pescada",
        "value": 20,
        "rarity": "Incomum"
    },
    {
        "nome": "Atum",
        "value": 22,
        "rarity": "Incomum"
    },
    {
        "nome": "Dourado-do-mar",
        "value": 25,
        "rarity": "Raro"
    },

    {
        "nome": "Garoupa",
        "value": 30,
        "rarity": "Comum"
    },
    {
        "nome": "Badejo",
        "value": 40,
        "rarity": "Incomum"
    },
    {
        "nome": "Linguado",
        "value": 50,
        "rarity": "Raro"
    },
    {
        "nome": "Bonito",
        "value": 60,
        "rarity": "Raro"
    },
    {
        "nome": "Tubarão",
        "value": 100,
        "rarity": "Raro"
    },
]

areas = {
    "Praia": {
        "level": 1,
        "fish": ["Robalo", "Sardinha", "Anchova", "Cavala", "Pargo"]
    },

    "Mar aberto": {
        "level": 3,
    "fish": ["Corvina", "Tainha", "Pescada", "Atum", "Dourado-do-mar"]
    },

    "Ilha misteriosa": {
        "level": 8,
        "fish": ["Garoupa", "Badejo", "Linguado", "Bonito","Tubarão"]
    }
}

def catch_fish(equipment,area):

    avaliable_fish = [
        fish_item
        for fish_item in fish
        if fish_item["nome"] in areas[area]["fish"]
    ]

    if equipment == "Vara Básica":
        weight = [30, 25, 20, 15, 10]

    elif equipment == "Vara Média":
        weight = [25, 22, 20, 18, 15]

    elif equipment == "Vara Profissional":
        weight = [20, 20, 20, 20, 20]

    return random.choices(
        avaliable_fish,
        weights = weight,
        k = 1
    )[0]



#catch = catch_fish()
# print(catch)