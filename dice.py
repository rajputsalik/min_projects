import os
import random 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dic(num_dice):
    history = []

    valid_commands = ['y', 'n', 'exit', 'clear', 'history']

    print("Type 'exit' to quit | 'clear' to clear screen | 'history' to view history\n")
    
    while True:
        user_input = input("Want To Roll The Dice? (y/n): ").lower()

        #  Invalid input check
        if user_input not in valid_commands:
            print("Invalid input! Allowed: y, n, exit, clear, history")
            continue

        # Exit
        if user_input in ['n', 'exit']:
            print("GoodBye")
            break

        # History
        elif user_input == 'history':
            print("\n History:")
            for item in history:
                print(item)
            print()
            continue

        #Clear
        elif user_input == 'clear':
            clear_screen()
            continue

        #Roll Dice
        elif user_input == 'y':
            roll_result = [random.randint(1, 6) for _ in range(num_dice)]
            history.append(roll_result)
            print("Result:", roll_result)


if __name__ == "__main__":
    num = int(input("Enter a number"))
    dic(num)