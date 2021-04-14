# Inheritance
# Accessing another classes is calles inheritance

class Songs:                                # Parent class / super class

    def name(self):
        print("People you know")

    def name2(self):
        print("Safe and sound")

class selena(Songs):                        # Child class/ sub class   - can access everything from parent class

    def info(self):
        print("American singer")

    def info2(self):
        print("Selena Gomez")

class swift(selena):                        # It can access both classes. Or if selena is not a child class then swift(selena,songs) - this will access both

    def info3(self):
        print("Taylor Swift")



s = Songs()
s2 = selena()
s3 = swift()


s.name()
s2.info2()
s3.info3()