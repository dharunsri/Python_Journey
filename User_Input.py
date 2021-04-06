# To get input from user

# Method 1

x = int(input("Enter the 1st number "))         # input() gets input from user
y = int(input("Enter the 2nd number "))

z = x+y

print(z)

# Method 2 [passing arguments from cmd]
"""
import sys
a = int(sys.argv[1])                            # argv - argument passes from the user. argv - present in the sys module
b = int(sys.argv[2])

c = a+b

print(c)  """

# Method 3
# Get a char
# from user
# But python has string only not a char datatype
# But this made gets only one char as input and print even user gave a string

ch = input("Enter a character: ")[0]
print(ch)

# Another method to evaluate a expression
# Here we use a function called eval
exp = eval(input("Enter a expression: "))
print(exp)