

# In computer we have heap memory and where all the objects get stored

class artist:
    pass

a1 = artist()                       # it takes space according to datatypes of variable and arguments
a2 = artist()

print(id(a1))           # each object have different addresses
print(id(a2))


class cars:

    def __init__(self):                     # Self - it takes itself as a argument
        self.brand = "Audi"
        self.color = "Black"                # Constructor - it decides the space required of an object
        self.cost = "40.5l"
        print(self.brand)
        print(self.color)

    def change(self):
        self.brand = "BMW"
        self.color = "White"
        self.cost = "40.5l"
        print(self.brand)
        print(self.color)

    def compare(self, other):
        if self.cost == other.cost:
            return True
        else:
            return False


c1 = cars()
c2 = cars()

if c1.compare(c2):
    print("They prices are same")
else:
    print("prices are different")
c1.change()