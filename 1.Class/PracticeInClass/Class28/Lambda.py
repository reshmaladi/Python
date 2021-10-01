#!C:\Python34
'''
def square (x):
	return  x*x
	
l= lambda y,z,m : (y*y ,z*z, m*m)
print (l(3,5,5))
print (type(l))

print (square(4))
'''
def generator(x):
	return lambda n:n+x

generator_of_5 = generator(7)
print (generator_of_5(5))

generator_of_10 = generator(8)
print (generator_of_10(10))