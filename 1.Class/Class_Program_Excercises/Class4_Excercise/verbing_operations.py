#!C:\Python34
a = input("Enter string : ")
if (len(a) <3):
	print (a)
elif(a.endswith("ing")):
	a=a.replace(a[-3:], "ly")
	print (a)
else:
	a= a+"ing"
	print (a)