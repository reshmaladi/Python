#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the numer of rows:"))
	for i in range(n):
		print( " " * i + "* " *(n-i))
'''
Enter the numer of rows:4
* * * *
 * * *
  * *
   *
'''