x=eval(input("Enter no1\t"))
y=eval(input("Enter no2\t"))
z=eval(input("Enter no3\t"))

def maxof(x,y,z):
	if x>y and x>z:
		print("max :" ,x)
	elif y>z:
		print("max :" ,y)
	else:
		print("max :" ,z)

maxof(x,y,z)