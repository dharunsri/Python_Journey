# Selection sort
# it takes 1st value and compare with all other value. if it is greater than other value it swaps
def sort(x):
    for i in range(len(n)-1):               # outer loop - set min value as 0,1,2,...
        min = i
        for j in range(i,len(n)):               # inner loop - compare all value with min
            if n[j]<n[min]:
                min = j
        n[min], n[i] = n[i], n[min]

    print(n)



n = [2,4,1,8,5,9,11,55,3,6]
sort(n)