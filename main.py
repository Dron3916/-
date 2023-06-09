import random

you_win = 0
computer_win = 0


def play_game(player_choice):
    global you_win, computer_win
    computer_choice = random.choice(["камень","ножницы","бумага",])

    player_choice = player_choice.lower()

    print(f"Ваш выбор: {player_choice}, компьютер выбрал {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья")
    elif(player_choice == 'камень' and computer_choice == 'ножницы') or\
            (player_choice == 'бумага' and computer_choice == 'камень') or\
            (player_choice == 'ножницы' and computer_choice == 'бумага'):
        you_win += 1
        print("Вы выиграли")
    else:
        computer_win += 1
        print("Компьютер выиграл")


while True:
    user_input = input("Выберите (Камень/Ножницы/Бумага) либо (q) для выхода либо (Счет) для показа счета: ")

    if user_input.lower() == "q":
        break
    if user_input.lower() == "счет" or user_input.lower() == "счёт":
        print(f"Ваш счет: {you_win}\nСчет компа: {computer_win}")
    if user_input.lower() not in ["камень","ножницы","бумага"]:
        print("Неправильный выбор")
    play_game(user_input)