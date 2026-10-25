player = {
  "name": "name",
    "health":100,
    "coins": 50,
    "turns":0,
    "inventory":[]
}
def show_status(player):
    print("твои характеристики")
    for key, values in player.items():
        print(key,"-",values)
    
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
        word = input("введи слово палиндром: ") .lower().strip()
        if word =="выйти":
            break
        reversed_word = word[:: -1]
        if word == reversed_word:
            print("молодец! у тебя появилась бутылочка живой воды!")
            player["inventory"].append("Бутылочка воды")
            solved = True
        else:
             print("попробуй еще раз")
        
    return player
   
# def look_around(health, coins):
#     print("\n Ты осматриваешься и видишь фонтан.")
#     print("\n хочешь живой воды, реши головоломку")
#     print("\n 1 - решить головоломку")
#     print("\n 2 - вернуться в центр")
#     action = input("твой выбор: ").lower().strip()
#     if action == 1 or "решить головоломку":


# def hotel(health,coins):
#     print("Ты нашла гостиницу")
#     if coins >=50:
#         health +=30
#         coins -=50
#         print(f"Ты выспалась у тебя {health} здоровья, твой баланс {coins} монеток")
#     else:
#         print("У тебя недостаточно денег")
#     return health, coins

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
    