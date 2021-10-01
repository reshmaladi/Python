#!C:\Python34
	
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	if fd != None:
		line = fd.readline()
		i=1
		line_numbers=[]
		while line != "":
			
			if(len(line) <= 80):
				print (line)
			else:
				line_numbers.append()
			i+=1	
			line = fd.readline()
	print ("Numbers are",	line_numbers)	
if __name__=="__main__":
	main()