import random

def get_user_choice():   # Вызываем варианты для выбора
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        print("Выбери камень, ножницы, бумагу или выход")
        choice = input().strip().lower()

        if choice == "выход":
            return None
        
        if choice not in choices:
            print("Не понимаю, о чём речь, давай попробуем сначала")
            continue

        return choice

def get_computer_choice(): # Генерация выбора компьютера
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ничья"
    if (user_choice == 'камень' and computer_choice == 'ножницы') or \
       (user_choice == 'ножницы' and computer_choice == 'бумага') or \
       (user_choice == 'бумага' and computer_choice == 'камень'):
        return "пользователь"
    return "компьютер"

def play_game(): # Выводим текстовые сообщение о ходе игры
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        print(f"Победитель: {winner}\n")

if __name__ == "__main__":
    play_game()