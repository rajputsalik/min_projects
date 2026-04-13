# By thrid variable

def swap(num , num1):

    num3 = num
    num = num1
    num1 = num3

    return num ,num1

    
num = int(input("Enter the number: "))
num1 = int(input("Enter the number: "))

print(swap(num,num1))


# without thrid variable
def swap(num , num1):

    num , num1 = num1 , num

    return num , num1

num = int(input("Enter the number: "))
num1 = int(input("Enter the number: "))

print(swap(num,num1))
