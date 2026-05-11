import random
secret = random.randint(1,10)
lives = 3

print ("Я загадал число от одного до 10! Попробуй угадать")

while True:
    guess = int(input("Твой ход: "))
    if guess == secret:
        print("Ура ты угадал!!!")
        break
    lives = lives - 1
    print(f"Неверно! У тебя осталось жизней: {lives}")
    
    if lives == 0:
        print(f"Ты проиграл. Было загадано число: {secret}")
        break
    elif guess < secret:
        print("Мое число больше")
    elif guess > secret:
        print("Мое число меньше")
