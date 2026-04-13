def cheeck_leap_year(num):
    if (num % 4 ==0 and num % 100 !=0) or num % 400 == 0:
        return f"{num} is leap year"
    
    else:
        return f"{num} is not leap year"
    

num = int(input("Enter the number: "))
print(cheeck_leap_year(num))    

