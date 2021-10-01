#!C:\Python34
import sys
from optparse import OptionParser

def copyfile(inputfile,outputfile, counttoline ):
	readfd = open(inputfile)
	writefd = open( outputfile,'w')
	
	line = readfd.readline()
	count =1
	while line != "":
		print ("Count", count , "count entered", counttoline)
		if (count > counttoline):
			break
		else:
			#writefd.write(str(count))
			writefd.write(line)
			line = readfd.readline()
			#writefd.write(line)
		count += 1
			
	else:
		print("complete file is copied")

	readfd.close()
	writefd.close()
	
def main():

#Check number of arguments are 4
	if (len(sys.argv) !=4):
		print ( "Enter all parameters" )
	
	else:
		inputfile = sys.argv[1]
		outputfile = sys.argv[2]
		counttoline = int(sys.argv[3])
		print (sys.argv)
		print (inputfile, outputfile, counttoline)
		copyfile(inputfile,outputfile, counttoline )
	


if __name__=="__main__":
	main()