#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the number of rows:"))
	for i in range(n):
		print( " " * (n-i)+ "* " * i)
	for i in range(n):
		print( " " * i + "* " *(n-i))
		
	print ( "Second approch")
	for i in range(n):
		print( " " * (n-i-1) + "* "*(i+1))
	for i in range(n-1):
		print(" "*(i+1) + "* "*( n-i-1))
'''
Enter the number of rows:4

   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''