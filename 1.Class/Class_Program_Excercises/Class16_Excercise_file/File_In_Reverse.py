#!C:\Python34
'''
def fileinrevserve(lines):
	if len(lines)== 0:
		return lines # for list [] , for string ""
	
	fileinrevserve(lines[1:])
	print (lines[0])
		
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")	
	lines = fd.read()
	lines= lines.split("\n")
	fileinrevserve(lines)
	

if __name__=="__main__":
	main()
	

'''
def fileinrevserve(fd):
	lines =fd.readline()
	if len(lines)== 0:
		return lines # for list [] , for string ""
	
	fileinrevserve(fd)
	print (lines)
		
def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")	
	fileinrevserve(fd)
	

if __name__=="__main__":
	main()
