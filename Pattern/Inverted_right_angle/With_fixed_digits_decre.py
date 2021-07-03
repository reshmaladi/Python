#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the numer of rows:"))
	for i in range(n+1):
		print ((str(n -i ) + " " ) * (n-i))
	print ()

'''
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''