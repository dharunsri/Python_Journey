# compile time error, logical error, run time error


# compile time error - syntax errors or syntatical error

# logical error - wrong output but program runs

# run time error - occurs by users. [ Ex: zerodivisionError ]


# statement - Normal statement and critical statement
#a = 10
#b = 0                           # it throws a runtime error

#print(a/b)

#print("Finished")               # so the program stops and it won't print it


a = 10
b = 0

try:
    print("Opened")                 # if we open a resourse
   # print(a/b)
    print("closed")            # it should be close. but when the condition getting a exception it won't close. it just jump to exception
    n = int(input("enter a value: "))
    print(n)                            # when the user give wrong input it throws an error

except ZeroDivisionError as e:          # and the statements print according to the error
    print("Sorry, can't divide a number by 0 ",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:                 # This is for all kind of error
    print("Something went wrong")
finally:                           # so we use finally. it'll print even you get or not exception
    print("closed")

print("Finished")