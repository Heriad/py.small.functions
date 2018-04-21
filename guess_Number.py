import random

rand_Number = random.randint(1, 10)

user_Guess = int(input("Choose the number between 1-10\n"))

list_Num = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
i = 0

for choose in range(1, 10):
    if user_Guess == rand_Number:
        print("You guessed it at the {number} time!".format(number=list_Num[i]))
        break
    else:
        print("You did not guess. Try again!")
        user_Guess = int(input("Choose another number between 1-10\n"))
    i += 1
