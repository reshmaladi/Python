#!C:\Python34

def togglebit(no, pos , bit):
	x= (1 << bit) -1
	x= (1 << bit) 
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	x = x << (pos- bit )
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	no = no | x 
	return no
	
def main():
	no = int (input ("enter the number"))
	pos = int (input ("enter the number"))
	bit = int (input ("enter the number"))
	print ("no , pos and bit are " , no, pos, bit)
	print (togglebit(no, pos, bit))
if __name__=="__main__":
	main()