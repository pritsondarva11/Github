import random

number = random.randint(1,100)
attempts = 0

print("Welcome to the Guessing Game!")
print("Guess a number between 1 to 100")

while True :
    guess = int(input("Enter Your Guess Number:"))
    attempts += 1 

    if guess < number:
        print("Too Low ")
    elif guess > number :
        print("Too High")
    else :
        print(f"Congrats you are in right in {attempts} attempts.")
        break 

