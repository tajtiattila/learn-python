import random

secret_num = random.randint(0, 100)
print("Guess my number between 0 and 100!")

def input_int(prompt):
    while True:
        s = input(prompt)
        if s.isdigit():
            return int(s)
        print("{} is not a number!".format(s))

num_guesses = 0
while True:
    n = input_int("Your guess: ")
    #n = int(input("Your guess: "))
    num_guesses += 1
    if n == secret_num:
        print("Correct, my number was {}.".format(secret_num))
        print("You guessed {} times.".format(num_guesses))
        break
    elif n > secret_num:
        print("My number is smaller.")
    else:
        print("My number is larger.")
