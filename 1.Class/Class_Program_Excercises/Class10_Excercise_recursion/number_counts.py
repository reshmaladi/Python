#!C:\Python34

def coutnone(x):
	if x ==0 :
		return  0
	return 1+ coutnone(x &(x-1))
	
def main():
	x= eval(input("enter first number"))
	#y= eval(input("enter second number"))
	print (coutnone(x))

if __name__=="__main__":
	main()
	
	
"""
count !=0
while (no!=0)
	count+=1
	no=no &(no-1)

"""