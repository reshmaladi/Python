#!C:\Python34
import os , stat

def file_stats(file):
	ret = os.access(file, os.F_OK)
	if ret == True:
		filemode = oct (stat.S_IMODE(os.lstat(file).st_mode))
		print ("File Permission is " ,filemode)
		
		
	
	

def main():
	file= input("Enter file: ")
	print (file_stats(file))


if __name__=="__main__":
	main()