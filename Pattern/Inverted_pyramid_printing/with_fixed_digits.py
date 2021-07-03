#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the number of rows:"))
	for i in range(n):
		print( " " * i + (str(i+1)+ " ") *(n-i))
'''

Enter the number of rows:3
1 1 1
 2 2
  3
'''