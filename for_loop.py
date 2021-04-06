# for loop

lst = [200, "selena", 219.23]

for i in lst:
    print(i)

name = "Selena Gomez"

for j in name:
    print(j)

# printing and sum of n numbers
sum = 0
for i in range(5):
    print(i)
    sum+=i
print("Total ",sum)

# in reverse order
for j in range (25,10,-2):
    print(j)

# printing perfect square between 1 & 50

for i in range(1,50):
    if i**2 == 50:
        print(i**2)
    else:
        break
