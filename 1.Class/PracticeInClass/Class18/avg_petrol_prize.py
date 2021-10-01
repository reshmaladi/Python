#!C:\Python34
def avg_petrol(file1, file2):
	fd = open(file1,"r")	
	sum_mh =0
	sum_goe =0 
	sum_kar=0
	mh =0
	count = 0
	if fd != None:
		line = fd.readline()
		while line != "":
			
			
			mh = line.split(sep=" ",maxsplit = 4)
			print (mh)
			print ("mh prize ", mh [2])
			print ("goa prize ", mh [3])
			print ("kar prize ", mh [4])
			
			sum_mh = sum_mh + int(mh[2])
			sum_goe = sum_goe + int( mh[3])
			sum_kar = sum_kar + int (mh[4])
			line = fd.readline()
			count +=1
			
		print (sum_mh, sum_goe, sum_kar)
			
	avg_mh = sum_mh// count
	avg_goe = sum_goe // count
	avg_kar = sum_kar// count
	print (avg_mh, avg_goe, avg_kar)
	
	fd_write = open(file2,"w")
	fd_write.write( str(avg_mh) + " " + str(avg_goe) + " " + str(avg_kar))
	fd_write.close()

def main():
	file1 = "C:\\1.Class\\PracticeInClass\\Class18\\petrolprize.txt"
	file2 = "C:\\1.Class\\PracticeInClass\\Class18\\avg.txt"
	avg_petrol(file1, file2)			
		

if __name__=="__main__":
	main()