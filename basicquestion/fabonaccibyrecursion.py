def fabonacci(num):
    if num <=1 :
        return num
    
    else:
        return fabonacci(num-1) + fabonacci(num-2)
    
num = int(input("Enter a number "))    
if num <= 0 :
    print("Enter a posive number ")
else:
     print("Fibonacci Sequence")
     for i in range(num):
         print(fabonacci(i) , end=" ")
    
    
   