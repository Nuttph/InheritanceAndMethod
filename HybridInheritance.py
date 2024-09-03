class GrandPa:
    def pGrandPa(self):
        print("Grandparents")

class Parent(GrandPa):
    def pParent(self):
        print("Parent")

class Child(Parent):
    def pChild(self):
        print("Child")


c1 = Child()

c1.pChild() # Child
c1.pParent() # Parent
c1.pGrandPa() # Grandparents