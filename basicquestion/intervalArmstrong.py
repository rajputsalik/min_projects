lower = int(input("Enter a lowe limit here: "))
upper = int(input("Enter a upper limit here: "))


for num in range(lower,upper+1):
    sum = 0 
    temp = num
    le = len(str(temp))
    while temp>0:
        digit = temp % 10
        sum += digit ** le
        temp//=10
    if num == sum:
        print(sum)    