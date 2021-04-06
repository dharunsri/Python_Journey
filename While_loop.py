# While loop

n = int(input("how many times? "))
i = 1                                           # initialisation
while i<=n:                                     # condition
    print("Looping ",i)
    i+=1                                        # increment or decrement

# Decrementing
j = n                                           # initialisation
while j>=1:                                     # condition
    print("Reverse ", j)
    j-=1                                        # decrement or increment

# Nested while

k = 1
while k<=n:
    print("Selena ", end="")
    l = 1
    while l<=3:
        print("Rocks-", end="")
        l+=1
    k+=1
    print()

# printing 1 to 100 and skipping which are divisible by 3 and 5
m =1
while m<=100:
    if m%3!=0 and m%5!=0:
        print(m)
    m+=1

# printing the pattern
t = 1
while t<=5:
    print("# ",end="")
    t2 = 1
    while t2<=4:
        print("# ",end="")
        t2+=1
    t+=1
    print()

