

print(__name__)
def wish():
    print("hello everyone", __name__)               # here __name__ will print __main__ but while using this code as module it will print module name

def songs():
    print("Lose You To Love Me")
    print("Dance Again")
    print("Back To You")


if __name__ == "__main__":                  # If we won't declare this condition then while importing it as a module it'll print everything
    wish()
    songs()