class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
    def say_hello(self):
        print("Hello from class B")
        super().say_hello()

class C(A):
    def say_hello(self):
        print("Hello from class C")
        super().say_hello()

class D(B,C):
    def say_hello(self):
        print("Hello from class D")
        super().say_hello()

# Creating an instance of D
obj_d = D()

# Calling the method
obj_d.say_hello()
