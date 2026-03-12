import random
secret = random.randint(1, 10)
guess = 0
while guess != secret:
    guess = int(input("Guess the number between 1 and 10: "))   
    if guess < secret:
        print("Too low, try again.")    
    elif guess > secret:
        print("Too high, try again.")
print("Congratulations! You guessed the number.")