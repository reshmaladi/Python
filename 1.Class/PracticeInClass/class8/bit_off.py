#!C:\Python34

def bitoff(num , pos):
	x=1
	#print (" number1   ", '{0:08b}'.format(1), end = "\n")
	x=x<<(pos-1)
	#print (" number1 after left shift  ", '{0:08b}'.format(x), end = "\n")
	#print (" number is ", '{0:08b}'.format(num), end= "\n")
	
	x=~x
	#print (" After negetion ",'{0:08b}'.format(x), end = "\n")
	num = num & x
	#print (" after addition ", '{0:08b}'.format(num), end = "\n")
	
	return num 

def main():
	#number, position = eval( input ("Enter two integers and position"))
	#print (number, position)
	print ( " after bit shift " ,  bitoff(185, 5))
		
if __name__=="__main__":
	main()