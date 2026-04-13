def even(num):
    if num % 2==0:
        return f"{num} is even number"
    
    else:
        return f"{num} is odd number "
    
num = int(input("Enter the number: "))
print(even(num))

