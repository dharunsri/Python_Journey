# Bubble sort

# Bubble sort takes 1st two values and compare if its big it swaps and then values get iterated and check for next 2 values and it continued


def sort(lst):
    for i in range(len(lst)-1,0,-1):                # outter loop - focus on total iteration
        for j in range(i):                                  # inner loop - focus on number of values compare
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    print(lst)

lst = [2,1,5,3,8,6]
sort(lst)