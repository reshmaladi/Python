#!C:\Python34

def reverselist(x):
	if len(x)== 0:
		return x # for list [] , for string ""
	
	reverselist (x[1:])
	print (x[0],end=" ")
	#y= (x[0])
	#return y 			# return x.appendx[0]

def main():
	x= eval(input("Enter elements of the list"))
	print ("Original List is", x)
	reverselist(x)

if __name__=="__main__":
	main()