# __name__ - special variable
# __init__ - special method


class artist:

    def __init__(self, name, song):                 # Special method - It calls itself according to objects.
        print("in init")
        self.name = name
        self.song = song

    def selena(self):
        print("Selena Gomez, the mezmerizing singer")
        print(self.name,self.song)


a1 = artist("selena", "De una vez")                     # here we have two objects(a1,a2) - so __init__ called 2 times
a2 = artist("Selan", "Lose you to love me")

a1.selena()
a2.selena()