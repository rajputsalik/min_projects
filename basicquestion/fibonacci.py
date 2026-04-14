num = int(input("Enter a number to find fibonacci sequence: "))
i , j = 0, 1
if num <= 0:
    print("Enter a positive number")
elif num == 1:
    print(i)
else:    
    print(i,j,end =" ")
    for _ in range(num-2):
        c= i +j
        print(c,end=" ")
        i = j
        j = c

        
    