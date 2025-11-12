import random
import os

class ScoreBoard:# Подсчёт результатов    
    def __init__(self, filename="scores.txt"):
        self.filename = filename
        self.player_score = 0
        self.computer_score = 0
        self.load_scores()

    def update_score(self, winner):
        if winner == "пользователь":
            self.player_score += 1
        elif winner == "компьютер":
            self.computer_score += 1

    def display_score(self):
        print(f"Счёт: Вы {self.player_score} : {self.computer_score} Компьютер")

    def save_scores(self):
        with open(self.filename, 'w') as f:
            f.write(f"{self.player_score},{self.computer_score}")

    def load_scores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    line = f.readline().strip()
                    if line:
                        p, c = map(int, line.split(','))
                        self.player_score = p
                        self.computer_score = c
            except Exception as e:
                print(f"Ошибка при загрузке счёта: {e}")
                self.player_score = 0
                self.computer_score = 0
        else:
            self.player_score = 0
            self.computer_score = 0

def get_user_choice(): # Выбираем значение
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        print("Выбери: камень, ножницы или бумага (или 'выход' для завершения)")
        choice = input().strip().lower()
        
        if choice == 'выход':
            return None
        
        if choice not in choices:
            print("Не понимаю о чём идёт речь, давай сыграе в игру")
            continue
        
        return choice

def get_computer_choice():# Выбор компьютера
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice): # Определяем победителя
    if user_choice == computer_choice:
        return "ничья"
    if (user_choice == 'камень' and computer_choice == 'ножницы') or \
       (user_choice == 'ножницы' and computer_choice == 'бумага') or \
       (user_choice == 'бумага' and computer_choice == 'камень'):
        return "пользователь"
    return "компьютер"

def play_game(): # Игровой цикл
    print("Давай сыграем в игру - 'Камень, ножницы, бумага'!")
    
    scoreboard = ScoreBoard()  # Создаём объект счёта
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice is None:
            print("Отлично поиграли!")
            break
        
        computer_choice = get_computer_choice()
        
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        print(f"Победитель: {winner}\n")
        
        scoreboard.update_score(winner)  # Обновляем счёт
        scoreboard.display_score()      # Показываем счёт
        scoreboard.save_scores()

if __name__ == "__main__":
    play_game()