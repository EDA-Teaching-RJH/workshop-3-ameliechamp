import random
secret_number = random.randint(1,10)
guess = int(input("What is my number?: "))

if guess > secret_number:
    print("Too high.")
elif guess < secret_number:
    print("Too low.")
else:
    print("Correct!")
