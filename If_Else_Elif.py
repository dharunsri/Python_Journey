# if - [checks the Condition]
# else - [if the condition not satisfied then it'll be print]

# Example 1 - Check the number is positive or negative
num = int(input("Enter any number: "))

if num>0:
    print("The number is positive")
else:
    print("The given number is negative")

# Example 2 - greatest among 3 numbers
# if checks the conditon
# if it is not satisfied elif conditon will be checked
# if nothing satisfied then else will be printed
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a>b and a>c:                     # If is a block. In python - called as "suite"
    print(a," is big")
elif b>c:                           # using elif - because it won't check wheather if condition is true. If we use if condition here it will check this too
    print(b, " is big")
else:
    print(c, "is big")

# Nested If
n = 10
if n>0:
    print("positive")
    if(n<=5):
        print("Less than or equal to 5")
    else:
        print("Greater than 5")

