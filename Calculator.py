# # I am creating Min Project Calculator

# def cal(*num , op):
    
#     if op == '+':
#          return sum(num)
#     elif op == '-':
#         result = num[0]
#         for n in num[1:]:
#             result -= n
#         return result
    
#     elif op == '*':
#         result = 1
#         for n in num:
#             result *= n
#         return result

#     elif op == '/':
#         result = num[0]
#         for n in num[1:]:
#             result /= n
#         return result

#     elif op == '%':
#         result = num[0]
#         for n in num[1:]:
#             result %= n
#         return result

#     else:
#         return "Enter proper operations"
                 


# if __name__ == "__main__":
    
#      print(cal(2,3, op='-'))
#      print(cal(10, 5, 2, op='+'))   
#      print(cal(10, 5, 2, op='-'))   
#      print(cal(10, 5, 2, op='*'))   
#      print(cal(10, 5, op='/'))      

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cal():
    history = []

    print("CLI Calculator")
    print("Type 'exit' to quit | 'clear' to clear screen | 'history' to view history\n")

    while True:
        user_input = input(">>> ") 
        if user_input.lower() == "exit":
            print("Goodbye")
            break
        
        elif user_input.lower() == "clear":
            clear_screen()
            continue

        elif user_input.lower() == "history":
            for item in history:
                print("\n📜 History:")
                print(item)
                print()  
                continue

        try:
            result = eval(user_input)
            output = f"{user_input} = {result}"
            print(output)
            history.append(output)

        except Exception as e:
            print("There is error, ",e)        
        

if __name__ == "__main__":
    cal()        



