# binary search

def search(lst,s):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    print(lst)

    l = 0
    u = len(lst)-1


    while l<=u:
        mid = (l + u) // 2
        if lst[mid] == s:
            print("found")
            break
        else:
            if lst[mid]< s:
                l = mid
            else:
                u = mid
    else:
        print("Not found")

lst = [2,4,1,6,3]
s = int(input("search value: "))
search(lst, s)