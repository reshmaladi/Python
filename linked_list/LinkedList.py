
class Node:
	__slots__ = "_element", "_next"
	
	def __init__(self, element, next):
		self._element = element
		self._next = next
		
class LinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None 
		self.size = 0
		
	def __len__(self):
		return self.size
		
	def isempty(self):
		return self.size == 0
		
	def addlast(self, e):
		newest = Node(e,None)
		if self.isempty():
			self.head = newest
		else :
			self.tail._next = newest
		self.tail = newest
		self.size +=1
		
	def display(self):
		p =self.head 
		while p:
			print (p._element,end = "-->")
			p= p._next
		print ()

s = LinkedList()
s.addlast(5)
s.addlast(6)
s.addlast(7)
s.display()
print(len(s))
s.addlast(2)
s.addlast(1)
s.addlast(7)
s.display()
print(len(s))
			
		
	