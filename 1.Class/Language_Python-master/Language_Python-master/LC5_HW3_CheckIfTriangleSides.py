x=eval(input("Enter no1\t"))
y=eval(input("Enter no2\t"))
z=eval(input("Enter no3\t"))
if x>y and x>z:
	a,b,c=x,y,z
elif y>z:
	a,b,c=y,z,x
else:
	a,b,c=z,x,y

if (b+c)>a :
	print(x,y,z,"can form a triangle")
else:
	print(x,y,z,"can't form a triangle")