#!C:\Python34

def issorted(x):
	flag=0
	i=0
	print (i, len(x))
	while i <(len(x)):
		print (i)
		if x[i]> x[i+1]:
			flag= 1
		i+=1	
		print (i)
		
			#return True
		#print (i, len(x))
		#return False


def main():
	x= eval(input("enter first number"))
	resp= issorted(x)
	print (resp)

if __name__=="__main__":
	main()