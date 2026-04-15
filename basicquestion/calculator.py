print("---------Mini Calculator")
num = float(input("Enter first number here: "))
num1 = float(input("Enter first number here: "))

print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

choice = int(input("Enter your Choice from (1-4): "))

match choice:
    case 1:
        result = "Addition"
    case 2:
        result = "Subtraction"
    case 3:
        result = "Multiplication"
    case 4:
         result = "Division"    
    case _:
        result = "unknown"



if choice == 1:
  print(f"You Have Choice {result}. The Addition of {num} and {num1} is {num + num1}")

elif choice == 2:
  print(f"You Have Choice {result}. The Subtraction of {num} and {num1} is {num - num1}")

elif choice == 3:
  print(f"You Have Choice {result}. The Multiplication of {num} and {num1} is {num * num1}")

elif choice == 4:
  print(f"You Have Choice {result}. The Division of {num} and {num1} is {num / num1}")

else:
  print(f"You Have Choice {result}. So,enter valid input")



