
#example of head recursion
# def message(n):
#     if(n==0):
#         print('Happy Bday')
#         return
#     print(f"{n} days left for the bday")
#     message(n-1)
# message(3)

#print 1->n numbers
# def display(n):
#     if(n==0):
#         return
#     display(n-1)
#     print(n)
# display(10)

#display 1-> even nos
# def display(n):
#     if(n==0):
#         return
#     display(n-2)
#     print(n)
# display(10)

#factorial
# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# print(fact('50'))

#sum of n numbers
# def add(n):
#     if(n==0):
#         return 0
#     return n+add(n-1)
# print(add(5))

#sum of n squares
def sum_sq(n):
    if(n==1):
        return 1
    return n*n+sum_sq(n-1)
print(sum_sq(4))