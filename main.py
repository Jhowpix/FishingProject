from player import Player

while True:
    name = input("\033[1;32m Qual o seu nome? \033[0m").strip()
    if name  and len(name) <= 12 and name.isalpha():
        break
    print("\033[1;33m Nome inválido. Use apenas letras, com no máximo 12 caracteres.\033[0m")

player = Player(name.upper())
print(f"\nBem vindo!, {player.name}!")
# player.fish()

while True:
    print("\n===\033[1;32m FISHING GAME \033[0m===\n")
    print("\033[1;32m1\033[0m - Pescar")
    print("\033[1;32m2\033[0m - Ver inventário")
    print("\033[1;32m3\033[0m - Ver status")
    print("\033[1;32m4\033[0m - Vender peixes")
    print("\033[1;32m5\033[0m - Comprar equipamentos")
    print("\033[1;32m6\033[0m - Escolher área")
    print("\033[1;32m7\033[0m - Sair")

    option = input("\n \033[1;32m Escolha: \033[0m \n")
    if option == "1":
        player.fish()

    elif option == "2":
        print(player.show_inventory())

    elif option == "3":
        print("\n===  \033[1;32m STATUS  ===\033[0m \n")
        print(f"Jogador: \033[1;35m{player.name}\033[0m")
        print(f"Nível: \033[1;35m{player.level}\033[0m")
        print(f"XP: \033[1;35m{player.xp}\033[0m")
        print(f"Dinheiro: \033[0;32m${player.money}\033[0m")
        print(f"Equipamento: \033[1;35m{player.equipment}\033[0m")
        print(f"Área: \033[1;35m{player.area}\033[0m")

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
        print(" \033[1;33m OPÇÃO INVALIDA.\n \033[0m Tente novamente.")

