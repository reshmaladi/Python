#!C:\Python34

a  = input ("Enter the sentence ")
print (len(a))
if len(a) <3:
	print (len(a))
if (len(a)) >=3 :
	print ("length is greater")
	if a.endswith('ing'):
		a= a[:3]+ 'ly'
	else :
		a += 'ing'
print (a)
	