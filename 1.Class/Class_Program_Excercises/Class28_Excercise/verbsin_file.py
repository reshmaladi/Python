import re

def main():
	fd = open("C:\\1.Class\\Class_Program_Excercises\\Class29_Excercise\\test.txt")
	data = fd.read()
	#print (data)
	for x in re.finditer("\w+ing", data, re.MULTILINE | re.IGNORECASE):
		print (x)
		print (x.start(), x.end(), data[x.start():x.end()])
	
if __name__ == "__main__":
    main()