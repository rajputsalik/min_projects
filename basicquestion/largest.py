def largest(num1 , num2 , num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is largest among {num2} and {num3}")

    elif num2 > num1 and num2 > num3:
      print(f"{num2} is largest among {num1} and {num3}")

    else:
        print(f"{num3} is largest among {num1} and {num2}") 
        
num = int(input("Enter the number: "))
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

largest(num,num1,num2)       