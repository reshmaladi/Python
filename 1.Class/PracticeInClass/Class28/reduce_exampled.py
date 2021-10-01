#!C:\Python34

import functools
def Multiply(x,y):
    print (x,y)
    return x*y

print(functools.reduce(Multiply, range(1,10)))