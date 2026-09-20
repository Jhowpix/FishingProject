from fish import catch_fish
from database import save_fishing_record

class Player:
    def __init__(self,name):
        self.name = name
        self.money = 100
        self.inventory = []
        self.equipment = "Vara Básica"
        self.level = 1
        self.xp = 0
        self.area = "Praia"

    def fish(self):
        caught = catch_fish(self.equipment, self.area)

        self.inventory.append(caught)

        print(f"VOCÊ PESCOU!\033[1;35m {caught['nome'].upper()}\033[0m")
        print(f"Valor:\033[1;35m {caught['value']}\033[0m")
        print(f"Raridade:\033[1;35m {caught['rarity'].upper()}\033[0m")

        xp_by_rarity = {
            "Comum": 5,
            "Incomum": 10,
            "Raro": 25,
            "Lendário": 50
        }

        xp = xp_by_rarity[caught['rarity']]

        self.gain_xp(xp)
        print(f"UP!\033[1;35m {xp}XP\033[0m")

        save_fishing_record(
            self.name,
            self.area,
            caught['nome'],
            caught['rarity'],
            caught['value'],
            xp,
            self.equipment
        )

    def  show_inventory(self):
        if not self.inventory:
            print("Inventário vazio.".upper())
            return

        print("\n=== \033[1;32m INVENTÁRIO \033[0m ===\n")

        for fish in self.inventory:
            print(
                f" \033[1;35m {fish['nome']}  | \033[0m "
                f" \033[1;35m {fish['value']} | \033[0m "
                f" \033[1;35m {fish['rarity']} \033[0m "
            )

    def sell_fish(self):
        if not self.inventory:
            print("\n \033[1;33m Você não possui peixes para vender.\033[0m ".upper())
            return

        total = sum(fish['value'] for fish in self.inventory)

        self.money += total
        self.inventory.clear()
        print(f" \033[1;33m Você vendeu os peixes por ${total}. \033[0m ".upper())

    def buy_equipment(self):
        print("\n=== \033[1;32m LOJA \033[0m ===")
        print(" \033[0;32m 1 \033[0m - Vara Média $100")
        print(" \033[0;32m 2 \033[0m - Vara Profissional $500")

        option = input(" \033[1;33m Escolha: \033[0m ")

        if option == "1":
            price = 100
            equipment = "Vara Média"

        elif  option == "2":
            price = 500
            equipment = "Vara Profissional"

        else:
            print(" \033[1;33m Opção invalida! \033[0m ".upper())
            return

        self.equipment = equipment

        if self.money >= price:
            self.money -= price
            print(f"Você comprou {equipment}")
        else:
            print(" \033[1;33m Dinheiro insuficiente! \033[0m ".upper())

    def gain_xp(self, amount):
        self.xp += amount

        xp_needed = self.level * 100

        if self.xp >= xp_needed:
            self.xp -= xp_needed
            self.level += 1
            print("-" * 20)
            print(f" \n \033[1;35m Você subiu para o nível {self.level}! \033[0m ".upper())
            print("-" * 20)

    def choose_area(self):
        print("\n===  AREAS  ===\n")

        print("1 - Praia")

        if self.level >= 2:
            print("2 - Mar aberto")
        else:
            print("2 - Mar aberto desbloqueia no nível 2.")

        if self.level >= 3:
            print("3 - Ilha misteriosa")
        else:
            print("3 - Ilha misteriosa desbloqueia no nível 3.")

        option = input(" \033[1;33m Escolha a área: \033[0m ")

        if option == "1":
            self.area = "Praia"

        elif option == "2":
            if self.level >= 2:
                self.area = "Mar aberto"
            else:
                print(" \033[1;33m Área bloqueada! \033[0m \n Você precisa estar no \033[1;32m nível 2.\033[0m ")
                return
        elif option == "3":
            if self.level >= 3:
                self.area = "Ilha misteriosa"
            else:
                print(" \033[1;33m Área bloqueada! \033[0m \n Você precisa estar no \033[1;32m nível 3.\033[0m ")
                return

        else:
            print(" \033[1;33m Opção invalida!\033[0m ".upper())
            return

        print(f"Você está agora em: {self.area}")
