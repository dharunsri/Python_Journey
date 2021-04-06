# Pattern 1

for i in range(4):
    for j in range(4):
        print('# ', end="")
    print()

print()

# Pattern 2
for i in range(1,5):
    for j in range(i):
        print('# ', end="")
    print()

print()

# Pattern 3
for i in range(5,0,-1):
    for j in range(i):
        print('# ', end="")
    print()

print()

#pattern 4
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()

print()

# Pattern 4
x,y='ABCD','PQR'
for i in range(4):
    print(x[:i+1]+y[i:])

