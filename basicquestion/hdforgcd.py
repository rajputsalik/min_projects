def findHCF(x,y):
    if x > y:
        smaller = x
    else:
        smaller = y    

    for i in range(1,smaller+1):
        if x % i ==0 and y % i ==0:
               hcf = i

    return hcf           
x = 12 
y = 30 

print(f"the hcf of the given two numbers is {findHCF(x,y)}")