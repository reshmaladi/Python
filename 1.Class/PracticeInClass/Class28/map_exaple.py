#!/usr/bin/python

def Square(x):
    return x*x

def IsEven(x):
	return (x&1) ==0
#x= map (IsEven , range(1, 30, 2))
f = filter(Square , range(1, 30))
for s in f:
	print (s)
#print (x)
#for y in x:
#	print (y)
#x = map(lambda x:x*x, range(1, 30, 2))

#help(x)