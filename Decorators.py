# Decorators

# Decorators modify on existing function
# It add extra features for existing function without changing the code

# For example, lets take a function and imagine it isn't exist here

def div(a,b):
    print(a/b)


# Using decorators we are modifying div function
def smart(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart(div)
div(10,200)

# Decorators - Change the behaviour of existing function

