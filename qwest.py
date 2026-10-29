player = {"name": "name", "health": 100, "coins": 50, "turns": 0, "inventory": []}


def show_status(player):
    print("твои характеристики")
    for key, values in player.items():
        print(key, "-", values)


def start():
    print("\nТы зашла в город. Твои действия:")
    print("  1. Идти вперёд")
    print("  2. Выйти")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice


def city_center():
    print("\n Ты пришла к центру города, куда двинешься дальше?")
    print("  1. Отдохнуть в гостинице")
    print("  2. Подкрепиться в местном кафе")
    print("  3. Осмотреться (фонтан)")
    print("  4. Выйти из игры")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice


def fountain(player):
    solved = False
    while not solved:
        word = input("введи слово палиндром: ").lower().strip()
        if word == "выйти":
            break
        reversed_word = word[::-1]
        if word == reversed_word:
            print("молодец! у тебя появилась бутылочка живой воды!")
            player["inventory"].append("Бутылочка воды")
            solved = True
        else:
            print("попробуй еще раз")

    return player


def main():
    global player

    print()
    print(" Добро пожаловать в Твинкс!")
    print()

    while player["health"] > 0 and player["coins"] >= 0:
        player["turns"] += 1
        show_status(player)
        choice = start()

        if choice == "1" or choice == "идти вперед":
            center_choice = city_center()

            if center_choice == "1":
                print(" Гостиница — в разработке")
            elif center_choice == "2":
                print(" Кафе — в разработке")
            elif center_choice == "3":
                player = fountain(player)
            elif center_choice == "4":
                print("\n Ты решила уйти. Спасибо за игру!")
                break
            else:
                print(" Неверный выбор.")

        elif choice == "2" or choice == "выйти":
            print("\n Ты решила уйти. Спасибо за игру!")
            break

        else:
            print(" Неверный выбор. Попробуй ещё раз.")


if __name__ == "__main__":
    main()
