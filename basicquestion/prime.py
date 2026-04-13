def prime(num):
    if num ==1:
       print("this is not  prime number")

    if num > 1:   
        for i in range(2,num):
            if num % i==0:
             print("this is not  prime number")
             break

        else:
            print("this is prime number")
                

num = int(input("Enter the number: "))
prime(num)