def factor(x):
    for i in range(1,x+1):
        if x % i ==0:
            print(i)


x =int(input("Enter a number to find the factor"))

print(f"the Factor of the given numbers is {factor(x)}")