#Это игра по угадыванию чисел
import random as rd

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = rd.randint(1, 20)
print("Что ж, " + myName + ", я загадываю число от 1 до 20.")

for guessesTaken in range(6):
    print("Попробуй угадать.")
    guess: int = int(input())

    if guess < number:
        print("Твое число слишком маленькое.")
    elif guess > number:
        print("твое число слишком большое.")
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Отлично, " + myName + "! ты справился за " + guessesTaken + " попытки!")

elif guess != number:
    number = str(number)
    print("Увы. Я загадал число " + number + ".")