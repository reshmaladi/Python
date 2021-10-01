#!C:\Python34

def square(x):
	return x*x
	
x= map(square , range (1,30, 2))
x =map(lambda x:x*x , range (1,30, 2))
print (x)
for y in x:
	print (y)