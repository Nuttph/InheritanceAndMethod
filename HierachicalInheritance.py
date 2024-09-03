class Parent:
    def PrintParent(self):
        print("Parent")

class ChildOne(Parent):
    def PrintChild(self):
        print("Child One")

class ChildTwo(Parent):
    def PrintChild(self):
        print("Child Two")

c1 = ChildOne()
c2 = ChildTwo()

c1.PrintParent() # Parent
c2.PrintParent() # Parent

c1.PrintChild() # Child One
c2.PrintChild() # Child Two