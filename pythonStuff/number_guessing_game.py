# the game randomly picks a number between 1 (lower_number) and 10 (higher_number) and user has to guess that number.
# user has only 3 (number_of_tries) tries

from random import randint

lower_number, higher_number = 1, 10
number_of_tries = 3
random_number: int = randint(lower_number, higher_number)
print(f"Guess the number between {lower_number} and {higher_number}.")

while True:
    
    if number_of_tries == 0:
        print("No more tries. You lose!")
        break
    
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if user_guess > random_number:
        number_of_tries -= 1
        print(f"Guessed number is too high! Tries remaining: {number_of_tries}")
    elif user_guess < random_number:
        number_of_tries -= 1
        print(f"Guessed number is too low! Tries remaining: {number_of_tries}")
    else:
        print("You guessed it!")
        break