import random

randomNumber = random.randint(1, 10)
i = 3

while i > 0:
    print('You  have ', i, 'tries left. Enter your number')
    inputNumber = int(input())
    if inputNumber == randomNumber:
        print('You won!')
        break
    else:
        print('You lose!')
        i = i - 1
print('Game Over')
