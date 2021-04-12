# In OOPs - Class or Static variable and Instance Variable


class games():

    app = "Playstore"                   # -> Class namespace    It belongs to all methods
    def __init__(self):
        self.name = "COC"
        self.genre = "War"              # -> Instance namespace   It belongs to one method

g1 = games()
g2 = games()

g2.genre = "Stats"                      # when instance variable modified it changes the value for one method

games.app = "Apk websites"              # when class variable modified it changes the value for all methods

print(g1.name, g1.genre, g1.app)
print(g2.name,g2.genre,g2.app)
