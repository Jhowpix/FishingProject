from fish import catch_fish

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

        print(f"Você pescou: {caught['nome']}")
        print(f"Valor: {caught['value']}")
        print(f"Raridade: {caught['rarity']}")

        xp_by_rarity = {
            "Comum": 5,
            "Incomum": 10,
            "Raro": 25,
            "Lendário": 50
        }

        xp = xp_by_rarity[caught['rarity']]

        self.gain_xp(xp)
        print(f"UP! {xp}XP")

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

        self.equipment = equipment

        if self.money >= price:
            self.money -= price
            print(f"Você comprou {equipment}")
        else:
            print("Dinheiro insuficiente!")

    def gain_xp(self, amount):
        self.xp += amount

        xp_needed = self.level * 100

        if self.xp >= xp_needed:
            self.xp -= xp_needed
            self.level += 1
            print(f"\n Você subiu para o nível {self.level}!")

    def choose_area(self):
        print("\n=== AREAS ===\n")

        print("1 - Praia")

        if self.level >= 3:
            print("2 - Mar aberto")
        else:
            print("2 - Mar aberto desbloqueia no nível 3.")

        if self.level >= 8:
            print("3 - Ilha misteriosa")
        else:
            print("3 - Ilha misteriosa desbloqueia no nível 8.")

        option = input("Escolha a área: ")

        if option == "1":
            self.area = "Praia"

        elif option == "2":
            if self.level >= 3:
                self.area = "Mar aberto"
            else:
                print("Área bloqueada! você precisa estar no nível 3.")
                return
        elif option == "3":
            if self.level >= 8:
                self.area = "Ilha misteriosa"
            else:
                print("Área bloqueada! você precisa estar no nível 8.")
                return

        else:
            print("Opção invalida!")
            return

        print(f"Você está agora em: {self.area}")
