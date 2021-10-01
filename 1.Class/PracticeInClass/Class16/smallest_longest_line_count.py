#!C:\Python34
	
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	if fd != None:
		line = fd.readline()
		minline = line
		maxline = line
		while line != "":
			line = fd.readline()
			if ( line =="\n" or line == ""):
				continue
			if len(line)> len(maxline):
				maxline =line				
			elif len(line) < len(minline):
				minline =line
		print ("Maximum Line = {} \n  minimum line = {} ". format( maxline,minline))

if __name__=="__main__":
	main()