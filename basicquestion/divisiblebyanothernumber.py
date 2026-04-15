# this is method done by loop

num = int(input("Enter a number "))

if num == 0:
     print("Cannot divide by zero")
else:
    print(f"Numbers divisible by {num} from 1 to 200:")
    for i in range(1,201):
        if i % num ==0:
            print(i)

# done by lambda fuction or anonymous function
n = int(input("\nHow many numbers you want in list: "))
ls =[]

for i in range(n):
    num = int(input("Enter a number: "))
    ls.append(num)

print("List:", ls)

nu = int(input("Enter divisor: "))
if nu == 0:
    print("Cannot divide by zero")
else:    
    Res = list(filter(lambda x : x % nu==0 ,ls))
    print(f"Numbers divisible by {nu} are:", Res)
