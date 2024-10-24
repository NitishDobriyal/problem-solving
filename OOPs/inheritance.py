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

# Creating instances of B and C
obj_b = B()
obj_c = C()

# Calling the methods
obj_b.say_hello()
print('--------------')
obj_c.say_hello()
