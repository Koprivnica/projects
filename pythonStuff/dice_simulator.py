# the program rolles number of dice

import random

def roll_dice(amount: int = 2) -> [int]:
    sum: int = 0
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
        sum += random_roll
        
    return rolls, sum

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll?")
            
            if user_input.lower() == "exit":
                break
            
            values = roll_dice(int(user_input))
            
            print(*values[0], sep = ", ")
            print(f"Total sum of values: {values[1]}")           
        
        except ValueError:
            print("Please, enter a valid number")
    
if __name__ == "__main__":
    main()     