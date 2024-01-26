import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry guess. too low.")
        elif guess > random_number:
            print("sorry guess. too high ")

    print(f"great the number is guessed{random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c
        feedback = input(f"Is {guess} to high (H), too low(L) or correct (c)??").lower()    
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess - 1
    print(f"yeah the computer guessed your number, {guess}, correct")  

computer_guess(1000)