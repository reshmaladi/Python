#!C:\Python34
def PalindromeOrNot(x):
	y = x[:len(x)//2]
	z = x[len(x)//2:]
	print (y, "   " , z)
	z= z[::-1]
	print("After reverse", z)
	if y==z:
		return True
	return False


def main():
	x = eval(input("Enter List list"))
	print (x)
	res= PalindromeOrNot(x)
	print(res)

	
if __name__=="__main__":
	main()
