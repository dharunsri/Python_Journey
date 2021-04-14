# File handling - accessing, creating or modifying a file

f = open("Example", "w")            # w - open a file to write

#f.write("This was created by the program")

a = open("Example","a")                 # a - append the date to the file
a.write("I'm appending the inputs")

f1 = open("pyvenv.cfg", "r")                # r - read everthing from a file
print(f1.read())

print()
#print(f1.readline(),end="")
#print(f1.readline())

#for i in f1:           # writes everthing from f1 to f
#    f.write(i)

"""
f = open("IMG", "rb")       # rb - to read images - in binary it reads
for i in f:
    print(i)
    
f1 = open("IMG","wb")       # wb - to write image - writes in binary
for i in f:
    f1.write(i)
"""