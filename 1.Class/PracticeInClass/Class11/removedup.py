#!C:\Python34
def remove_dup(x, el):
	while el in x:
		x.remove(el)
def remove(x,el):
	for i in x:
		#print ("i", i ,  "el is", el, "\n")
		if el ==i :
			x.remove(el)

def main():
	x= eval(input("enter list"))
	el= eval(input("enter element which you want to remove"))
	print (x)
	remove_dup(x, el)
	print (x)

if __name__=="__main__":
	main()