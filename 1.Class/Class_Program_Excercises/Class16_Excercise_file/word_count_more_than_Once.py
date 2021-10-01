#!C:\Python34
#import fileIO


def main():
	fd = open("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	word = input("enter the word")
	#lines = io.fileIO("C:\\1.Class\\PracticeInClass\\Class16\\test.txt")
	lines = fd.readline()
	print (lines)
	while lines != b"":
		if str(lines).count(word) >1 :
			print (lines)
		lines = fd.readline()

if __name__=="__main__":
	main()