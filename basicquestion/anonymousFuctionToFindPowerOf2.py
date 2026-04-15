num = int(input("Enter a number"))
res = list(map(lambda x : 2**x , range(num+1)))

print(res)

for i in range(num+1):
    print("The valuue of 2 raised to power",i,"is",res[i])