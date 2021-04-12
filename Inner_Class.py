# declaring a class inside a class


class great:

    def __init__(self):
        self.name = "Elon Musk"
        self.comp = "Tesla"
        self.info = self.info()

    def show(self):
        print(self.name,self.comp)
        self.info.show()                                        # access show() method from inner class

    class info:                                                 # inner class

        def __init__(self):
            self.comp1 = "Space X"
            self.comp2 = "Solar City"
            self.comp3 = "Boring Company"
        def show(self):
            print(self.comp1,self.comp2,self.comp3)




g1 = great()

i = g1.info
g1.show()




