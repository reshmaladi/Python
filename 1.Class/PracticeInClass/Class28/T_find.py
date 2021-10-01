#!C:\Python34
import re

def main():
	fd = open( "C:\\1.Class\\PracticeInClass\\Class28\\audio.conf")
	data = fd.read()
	#ob = re.compile( r"\bt\w+e\b", re.IGNORECASE)
	ob = re.compile( r"\b\w+e\b", re.IGNORECASE)
	for match in ob.finditer(data):
		print ( match) 

if __name__ == "__main__":
    main()


