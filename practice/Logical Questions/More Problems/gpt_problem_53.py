# Method Overriding
# Create:
# Class Animal with method sound() that prints "Animal makes sound"
# Class Dog inherits Animal and overrides sound() to print "Dog barks"
# Call method using Dog object.

class Animal:

    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

