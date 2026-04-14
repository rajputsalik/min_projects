# by recursion method

def fac(num):
    if num == 0:
     return 1
    else:
       return ((num) * fac(num-1))
    

fact = int(input("Enter a number to find factorial: "))
result = fac(fact)
print(f"The factorial of {fact} is {result}")

# by loop

fact = int(input("Enter a number to find factorial: "))
fac = 1

if fact == 0:
     print("the factorial of 0 is", 1)

if fact < 0:
   print("factorial of negative does not exist")

if fact > 0:
    for i in range(1,fact+1):
       fac = fac * i

print(f"the factorial of {fact} is {fac}")