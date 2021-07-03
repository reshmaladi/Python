#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the numer of rows:"))
	for i in range(n+1):
		print ((str(i+1) + " " ) * (n-i))
	print ()
'''
Enter the numer of rows:6
111111
22222
3333
444
55
6
'''