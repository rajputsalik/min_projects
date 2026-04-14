tabl = int(input("Enter a number to write a table: "))

for i in range(1,11):
    print(f"{tabl} * {i} = {tabl * i}")

# by while loop 

tab = int(input("Enter a number to write a table: "))
i = 1

while i<=10:
     print(f"{tab} * {i} = {tab * i}")
     i +=1
