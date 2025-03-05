#Python Program to Understand Variable Copies and References Using id() Function

import copy

# immutable objects
x = 10
y = x
print(id(x))
print(id(y))
y = 20
print(x , y)
print(id(y))

# mutable objects

a = [10, 20, [30,40]]
b=copy.copy(a)
print(a , b)
print(id(a))
print(id(b))
b[1]=100
b[2][0]=50
print(a , b)

c=copy.deepcopy(a)
print(a , c)
print(id(a))
print(id(c))
c[1]=100
c[2][0]=50
print(a , c)
