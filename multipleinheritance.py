class A:
    def __init__ (self):
        super().__init__()
        print("A Constructor")
class B(A):
    def __init__ (self):
        super().__init__()
        print("B Constructor")
class C(B):
    def __init__ (self):
        super().__init__()
        print("C Constructor")
class D(C,B):
    def __init__ (self):
        super().__init__()
        print("D Constructor")

obj=D()        