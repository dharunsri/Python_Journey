# using yield keyword makes a function as generator

def ten():
    n =1

    while n<=10:
        sq = n*n
        yield sq

        n +=1

val = ten()

for i in val:
    print(i)