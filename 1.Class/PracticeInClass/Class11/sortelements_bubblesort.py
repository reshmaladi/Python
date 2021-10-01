#!C:\Python34
# Bubble sort 
def sorted(x):
	for i in range(len(x)-1):
		for j in range (i+1, len(x)):
			print (x[i] , x[j])
			if (x[i] > x[j]):
				temp = x[i]
				x[i] = x[j]
				x[j] = temp
		

def main():
	x= eval(input("enter list"))
	sorted(x)
	print (x)

if __name__=="__main__":
	main()