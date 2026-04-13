import random 

def guess_number():
    yes_no = input("Want to Play the game (y/n)").lower()

    if yes_no == 'n':
       print("Good Bye..")
       return False
    
    limit = 5
    number = random.randint(1, 100)
    print("You have only 5 guesses")
    
    while limit > 0:
        user_input = input("Enter a number between (1-100): ")

        if not user_input.isdigit():
            print("Enter a valid number")
            continue
        user_input = int(user_input)

        if number > user_input:
          print("Every low..")

        elif number < user_input:
          print("Every High..")
        else:
          print("You Guessed right.. The Number was" , number) 
          return True

        limit -=1
        print(f"Attempts left: {limit}")

    print("Game Over! Number was:", number)   
    return True
while True:
   result = guess_number()
   if result == False:
      break
   
   again = input("\n Want to play agai? (y/n: )").lower()

   if again =='n':
      print("Good bye..") 
      break