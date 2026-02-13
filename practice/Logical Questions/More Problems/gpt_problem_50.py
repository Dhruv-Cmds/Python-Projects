# Multiple Inheritance
# Create:
# Class A → method showA()
# Class B → method showB()
# Class C inherits A and B
# Call both methods using object of C.

class A:
    def showA(self):
        pass

class B:
    def showB(self):
        pass

class C(A , B):
    pass

a = A()
b = B()
c = C()

c.showB()
c.showA()