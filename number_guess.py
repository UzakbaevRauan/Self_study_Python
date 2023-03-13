import random
num = random.randrange(1,100)
guess = int(input())
while num != guess:
    if num > guess:
        print("Too high!")
        guess = int(input())
    else:
        print("Too Low!")
        guess = int(input())
print('Nice')
