class A:
    def PrintA(self):
        print("A")
class B(A):
    def PrintB(self):
        print("B")
class C(B):
    def PrintC(self):
        print("C")

c1 = C()

c1.PrintA() # A
c1.PrintB() # B
c1.PrintC() # C