from fish import catch_fish

class Player:
    def __init__(self,name):
        self.name = name
        self.money = 100
        self.inventory = []
        self.equipment = "Vara Básica"

    def fish(self):
        caught = catch_fish(self.equipment)

        self.inventory.append(caught)

        print(f"Você pescou: {caught['nome']}")
        print(f"Valor: {caught['value']}")
        print(f"Raridade: {caught['rarity']}")

    def show_inventory(self):
        if not self.inventory:
            print("Inventário vazio.")
            return

        print("\n=== INVENTÁRIO ===\n")

        for fish in self.inventory:
            print(
                f"{fish['nome']}  | "
                f"{fish['value']} | "
                f"{fish['rarity']}"
            )

    def sell_fish(self):
        if not self.inventory:
            print("\nVocê não possui peixes para vender.")
            return

        total = sum(fish['value'] for fish in self.inventory)

        self.money += total
        self.inventory.clear()
        print(f"Você vendeu os peixes por ${total}.")

    def buy_equipment(self):
        print("\n=== LOJA ===")
        print("1 - Vara Média $100")
        print("2 - Vara Profissional $500")

        option = input("Escolha: ")

        if option == "1":
            price = 100
            equipment = "Vara Média"

        elif  option == "2":
            price = 500
            equipment = "Vara Profissional"

        else:
            print("Opção invalida!")
            return


        if self.money >= price:
            self.money -= price
            print(f"Você comprou {equipment}")
        else:
            print("Dinheiro insuficiente!")