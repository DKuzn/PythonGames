#Это игра по угадыванию чисел
import random as rd

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = rd.randint(1, 100)
print("Что ж, " + myName + ", я загадываю число от 1 до 100.")

for guessesTaken in range(12):
    print("Попробуй угадать.")
    guess: int = int(input())

    if guess < number:
        print("Твое число слишком маленькое.")
    elif guess > number:
        print("Твое число слишком большое.")
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Отлично, " + myName + "! ты справился с " + guessesTaken + " попытки!")

elif guess != number:
    number = str(number)
    print("Увы. Я загадал число " + number + ".")