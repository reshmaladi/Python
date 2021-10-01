#!C:\Python34
class stack:
	def __init__(self, size):
		print ("Stack constractured of size", size)
		self.stack = []
		self.__size =size
		#print self.stack
		
	def push(self,data):
		status ="Failed"
		if not self.isFull():
			self.stack.append(data)
			print (data, "Pushed to stack")
			status = "Passsed"
		return status
		
	def pop(self):
		status ="Failed"
		data = -1
		if not self.isEmpty():
			self.stack.pop()
			print ("Data is poped from stack")
			status = "Passsed"
		return data, status
		
	def isFull(self):
		return len(self.stack)  == self.__size
		
	def isEmpty(self):
		return (self.stack == [])
		
	def stacksize(self):
		print (len(self.stack))
	def printintersting(self):
		try:
			print ("Inersting" , self.intserting)
		except:
			print (" not inerting")
		
		
	def __del__(self):
		print ("Stack distructor")
		del self.stack
def main():
	st =stack(10)
	print (st._stack__size)
	''''
	st =stack(10)
	st.push(1)
	st.push(2)
	print (st.__dict__)
	st.intserting =True
	st.printintersting()
	st1= stack(10)
	st1.push(3)
	print (st1._stack__size)
	print (st._stack__size)
	print (st.__dict__)
	print (stack.__dict__)
	st1.printintersting()
	st.stacksize()
	st.pop()
	st.stacksize()
	
	'''
	
if __name__=="__main__":
	main()
		