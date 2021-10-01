#!C:\Python34

s1 =input("Enter first string to check if it is rotational " )
s2 =input("Enter second string to check if it is rotational " )
s1 = s1+ s1
print (s1)
if s2 in s1:
	print ("Rotational")
else: 
	print ("Not Rotational")
