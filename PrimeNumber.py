# Prime Number

num = int(input("Enter num to check"))

for i in range(2,num):
    if num%i==0:
        print("Not a prime")
        break
else:
    print("Prime number")