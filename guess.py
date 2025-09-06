import random
print("Welcome to number guessing game.\n")

right_number = random.randint(1,5)

print("I've picked a number for you to guess.")
print("The number is between 1 and 5.\n")

guessed_number = int(input("Guess a number:\n"))

while right_number != guessed_number: 
    if guessed_number < 1 or guessed_number > 5:
        print("Invalid guess. Please enter a number between 1 and 5.")
    else:
        if guessed_number<right_number:
            print("Choose a higher number.\n")
        elif guessed_number > right_number:
            print("Choose a lower number.\n")
        guessed_number =int(input("Enter guess number again: "))

print("\nCorrect guess.")
print("You won. Thank you for playing.")
