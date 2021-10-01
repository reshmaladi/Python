#!C:\Python34

a = input ("Enter a ")
b = input ("Enter b ")
print (len(a) , len(b))
print ("With string addition")
if ( b in (a + a)):
	print ("Rotational")
else: print ("not rotational")
print ("With string multiply by 2")
if a in (b *2):
	print ("Rotational")
else: print ("not rotational")
