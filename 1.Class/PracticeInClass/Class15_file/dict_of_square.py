#!C:\Python34
def numb_sqaure(n):
	result= {}
	for i in range(1,n+1):
		result[i] = i*i
	return result
	
def main():
	n = int(input("Enter number "))
	result = numb_sqaure(n)
	print(result)

		
if __name__=="__main__":
	main()