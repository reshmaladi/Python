#!C:\Python34

def togglebit(no, pos , bit):
	x= (1 << bit) -1
	x= (1 << bit) 
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	x = x << (pos- bit )
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	return no ^ x	

def main():
	no = int (input ("enter the number"))
	pos = int (input ("enter the number"))
	bit = int (input ("enter the number"))
	print ("no , pos and bit are " , no, pos, bit)
	print (togglebit(no, pos, bit))
if __name__=="__main__":
	main()
	
	
'''
	00000111010
^
	00000001111
	============
	00000110101



(no & x) ==0 
x =x << 1
return (no & ~x
'''