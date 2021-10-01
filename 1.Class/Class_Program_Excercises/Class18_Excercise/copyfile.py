#!C:\Python34
# Copying file from one file to another

import sys
import argparse
import shutil

def copyfile(inputfile,outputfile, counttoline ):
	readfd = open(inputfile)
	writefd = open( outputfile,'w')
	
	if counttoline ==0:
		shutil.copyfileobj(readfd,writefd)
	else:
		line = readfd.readline()
		count =1
		while line != "":
			#print ("Count", count , "count entered", counttoline)
			if (count > counttoline):
				break
			else:
				writefd.write(line)
				line = readfd.readline()
				count += 1
			
		else:
			print("complete file is copied")

	readfd.close()
	writefd.close()
	
def main():
	print (sys.argv)
	parser= argparse.ArgumentParser()
	parser.add_argument("-i", type=str, help="Input/source file", required =True)
	parser.add_argument("-d", type=str, help="Destination file",required = True)
	parser.add_argument("-n", type=int, help="number of files to be copied" ,default= 0)
	args = parser.parse_args()
	print (args)
	copyfile(args.i,args.d,args.n)


if __name__=="__main__":
	main()