#!C:\Python34
n =[ int(x) for x in input("Enter space separated elements of list: ").split(" ")]
print (*n)
min_c = n[0]
#print (n[0])
for i in n:
	if i < min_c:
		min_c = i
print (min_c)