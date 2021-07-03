#!C:\Python34
def move_digits(l1):
	j= 0
	for num in l1:
		if num != 6:
			l1[j] = num
			j+=1
	for n in range(j,len(l1)):
		l1[n] =0
	print(l1)

l1= [2,4,1,6,5,7,6,2,6,1,6,6,9]
move_digits(l1)