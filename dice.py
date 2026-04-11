import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dic():
    his = []
    print("Type 'exit' or 'No' to quit | 'clear' to clear screen | 'history' to view history\n")
    print("Want To Roll The Device? (y/n): ")
    while True:
        user_input = input(">>> ") 
        if user_input.lower() == 'n' or user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'y':
            continue

        elif user_input.lower() == 'history':
            for item in his:
                his.append(item)
                print()
                continue

        elif user_input.lower() == 'clear':
            clear_screen()
            continue

        try:
            print("Playing")

        except Exception as e:
            print("Invaild Input ",e)     
if __name__ == "__main__":
    dic()        

