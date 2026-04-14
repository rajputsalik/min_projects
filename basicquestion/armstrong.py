num = int(input("Enter a number here: "))
le = len(str(num))  # find the the length of thw digit or counting the digit
sum=0
temp = num # store the orignal number in another variable
while temp > 0: 
    digit = temp %10 # take last digit of the number 
    cube = digit** le # doing the cube of that number 
    sum = sum + cube # sum of the cube 
    temp//=10 # thwn remoiving the last digit from the number 

if(sum==num):# cheeck the sum is equal to orignal number or not 
    print("It is an armstrong number")

else:
    print("It is not an armstrong number")



