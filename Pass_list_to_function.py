# Passing a list to fuction

l = []
n = int(input("Range of list: "))
for i in range(n):
    x = int(input("Enter the values: "))
    l.append(x)
print(l)

def check(l):
    even = 0
    odd = 0
    for i in l:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd
even, odd = check(l)

print("Even : {} and odd : {}".format(even,odd))


# Example

names = []
m = int(input("How many names? "))
for j in range(m):
    name = str(input("Enter the names: "))
    names.append(name)
def spell(names):
    for k in names:
        if len(k) >=5:
            print(k)

spell(names)
