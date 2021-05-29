#!C:\Python34
l1 = [int(i) for i in input().split()]
d =int(input())

#Approch 1
for i in range(0,len(l1)):
	num_to_find = d - l1[i]
	for j in range(i+1,len(l1)):
		if num_to_find == l1[j]:
			print("Printing with I approach :", i, j)
			
#Approch 2
m ={}
for i in range(0,len(l1)):
	num_to_find = d - l1[i]
	if num_to_find in m:
		print ("Printing with 2 approach :", i , m[num_to_find])
	m[l1[i]] = i


