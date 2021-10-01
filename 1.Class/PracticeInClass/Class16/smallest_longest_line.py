#!C:\Python34
	
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	if fd != None:
		line = fd.readline()
		i=1
		line_numbers=[]
		line = fd.readline()
		while line != "":
			line_numbers.append(len(line))
			line = fd.readline()
			print (line_numbers)
	line_numbers.sort()
	print ("smallest", line_numbers[0])
	print ("greatest", line_numbers[0])
if __name__=="__main__":
	main()