#!C:\Python34

def patterndouble(n):
	for i in range (1, n+1):
		k = i 
		for _ in range (1, i+2):
			print(k, end=' ')
			k *=2
		print ( " " , end= "\n")
	
	
def main():
	no= eval(input ("enter the number"))
	
	print (patterndouble(no))

if __name__=="__main__":
	main()
	
	
	
'''
Pattern output
1 2
2 4 8
3 6 12 24
4 8 16 32 64

'''