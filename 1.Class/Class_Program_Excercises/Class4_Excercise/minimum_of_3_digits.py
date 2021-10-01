#!C:\Python34
a,b,c= eval(input("Enter three numbers "))
print ("a= " , a, "b= ", b , "c= ", c)

if (a<b and a<c):
	print (a , "is smaller")
elif ( b<c and b <a):
	print (b , "is smaller")
else:
	print (c , "is smaller")