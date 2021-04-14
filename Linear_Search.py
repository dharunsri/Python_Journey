# Linear search

def search(lst,s):
    i = 0
    while i<len(lst):
        if lst[i]==s:
            print("Found")
            break
        i += 1
    else:
        print("Not found")


lst = []
n = int(input("Enter limit"))
for i in range(n):
    x = int(input("Enter value: "))
    lst.append(x)
print(lst)
s = int(input("Enter the number"))
search(lst,s)