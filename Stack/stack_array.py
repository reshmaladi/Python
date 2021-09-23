#!C:\Python34
class  stack_array:
	def __init__(self):
		self.data = [] #
	
	def __len__(self):
		return len(self.data)
		
	def isempty(self):
		return len(self.data) == 0
		
	def push(self,element):
		self.data.append(element)
		
	def pop(self):
		if self.isempty():
			print ("Stack is empty")
			return 
		else: self.data.pop()
		
	def top(self):
		if self.isempty():
			print("Stack is empty")
			return
		else: return self.data[-1]
		
s = stack_array()
s.push(3)
print(s.data)
s.push(5)
s.push(6)
s.push(8)
s.push(1)
print("After insersion",s.data)
print(s.pop())
print("After pop",s.data , "and lenght", len(s))
print(s.top())
print("after top", s.data)
