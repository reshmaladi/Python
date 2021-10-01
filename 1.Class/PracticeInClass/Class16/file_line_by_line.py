#!C:\Python34
	
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	if fd != None:
		line = fd.readline()
		#print (line)
		while line != "":
			print (line)
			line = fd.readline()
		
if __name__=="__main__":
	main()