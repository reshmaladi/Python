import threading

path = 'C:\\Users\\reshma.ladi\\Documents\\GitHub\\Python\\selfpractice\\'
def task1(n):

	even = open(path+ "\\even.txt", "w") 
	for i in range(n):
		if i%2 == 0:
			even.write( str(i)+ " ")
	even.close()

def task2(n):

	with open(path +"\\odd.txt", "w") as odd:
		for i in range(n):
			if i%2 != 0:
				odd.write(str(i) + " ")
			
	odd.close()
	
def replace_content():
	with open(path +"\\replace.txt", "r") as re:
		content = re.read()
	new = content.replace("good", "best")
	with open(path +"\\replace.txt", "w") as wr:
		wr.write(new)
	wr.close()

if __name__ == "__main__":
	n=10
	t1 = threading.Thread(target= task1 , args = (n,))
	t2 = threading.Thread(target =task2, args = (n,))
	t3 = threading.Thread(target =replace_content, args = ())
	
# creating threads
	#t1 = threading.Thread(target=task1, args=( n,),name='t1')
	#t2 = threading.Thread(target=task2,args=(n,), name='t2')

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

