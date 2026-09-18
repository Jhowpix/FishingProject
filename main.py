from player import Player

while True:
    name = input("Qual o seu nome? ").strip()
    if name  and len(name) <= 12 and name.isalpha():
        break
    print("Nome inválido. Use apenas letras, com no máximo 12 caracteres")

player = Player(name)
print(f"\nBem vindo, {player.name}!")
# player.fish()

while True:
    print("\n=== FISHING GAME ===")
    print("1 - Pescar")
    print("2 - Ver inventário")
    print("3 - Ver status")
    print("4 - Vender peixes")
    print("5 - Comprar equipamentos")
    print("6 - Escolher área")
    print("7 - Sair")

    option = input("Escolha: ")
    if option == "1":
        player.fish()

    elif option == "2":
        print(player.show_inventory())

    elif option == "3":
        print("\n=== STATUS ===\n")
        print(f"Jogador: {player.name}")
        print(f"Nível: {player.level}")
        print(f"XP: {player.xp}")
        print(f"Dinheiro: ${player.money}")
        print(f"Equipamento: {player.equipment}")
        print(f"Área: {player.area}")

    elif option == "4":
        player.sell_fish()

    elif option == "5":
        player.buy_equipment()

    elif option == "6":
        player.choose_area()

    elif option == "7":
        print("Até mais!")
        break

    else:
        print("Opção invalida. Tente novamente.")

