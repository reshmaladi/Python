#!C:\Python34
	
def main():
	#file = "C:\1.Class\14.23rdFeb.txt"
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	#print(fd.readlines())
	print (fd.read(2))
	print ("++++ \n")
	print (fd.read())
	print ("++++ \n")
	print (fd.read())	
	print ("++++\n")
	print(fd.readlines())
		
if __name__=="__main__":
	main()