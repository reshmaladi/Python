#!C:\Python34
if __name__ == "__main__":
	n =int(input("Enter the numer of rows:"))
	for i in range(n):
		print (" " * (n-i-1), end ="")
		for j in range(i+1):
			print (j+1, end = " ")
		print()