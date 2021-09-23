
def rotate(n, d):

	rgt = []
	#print(len(n)-d)
	for i in range(len(n)-d,len(n)):
		rgt.append(n[i])
	print (*rgt)
	return (rgt + n[0:len(n)])

if __name__ == "__main__":
	d = 2
	print("User input")
	lst = [int(x) for x in input().split()]
#print (*lst)
	l =rotate(lst, d)
	print(l)