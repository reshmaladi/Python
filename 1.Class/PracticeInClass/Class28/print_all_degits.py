#!C:\Python34
import re

def main():
	fd = open( "C:\\1.Class\\PracticeInClass\\Class28\\audio.conf")
	data = fd.read()
	ob = re.compile( r"\d+")
	for match in ob.finditer(data):
		print ( match) 

if __name__ == "__main__":
    main()
