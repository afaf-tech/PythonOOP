# diamond problem

class A:
    def show(self):
        print("ini adlah show a")

class B(A):
    # def show(self):
    #     print("ini adlah show B")
    pass
class C(A):
    def show(self):
        print("ini adlah show C")

class D(B,C):
    pass
    # def show(self):
    #     print("ini adlah show B")

objek = D()
objek.show()
