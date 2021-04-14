# poly - Many ; Morph - forms

# 4 types - Duck Typing, Operator overloading, Method Overloading, Method Overriding


# Duck Typing

class python:

    def execute(self):
        print("Functional programming")
        print("Procedural programming")
        print("Object oriented programming")

class python2:

    def execute(self):
        print("in year 1989")
        print("lots of libraries")


class language:

    def code(self,program):
        program.execute()

program = python()
program2 = python2()
lang = language()

lang.code(program2)


# Duct typing - used in dynamic language. "If it looks like a duck, quacks lika a duck, its a duck"
# Like wise, here if the method has an execute method then its enough. We don't mind about which class it is.. we just need a execute method that's it.
