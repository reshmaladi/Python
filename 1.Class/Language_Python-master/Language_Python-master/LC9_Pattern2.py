def patt(n):
	i="*\t"
	j="\t"
	for x in range(1,n,1):
		print(str(j*(n-x))+str(i*x))
'''	
	for i in range(1,n):
		for _ in range(n-i):
			print("\t",end="")
		for _ in range(i):
			print("*\t",end="")
		print()
			
		
	
	
	'''
def main():
	x=eval(input("Enter number of rows"))
	patt(x+1)
	
	
	
if __name__=="__main__":
	main()