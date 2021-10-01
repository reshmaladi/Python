#!C:\Python34

class student:
	auto_roll_no =1
	def __init__(self, name, address, dob, course, division):
		self.__roll_no = student.auto_roll_no
		student.auto_roll_no +=1
		self.__name = name
		self.__address = address
		self.__dob =dob
		self.__course = course
		self.__division =division
		self.__marks= dict()
	def getName(self):
		return self.__name
	def getAddress(self):
		return self.__address
	def getdob(self):
		return  self.__dob
	def getcource(self):
		return self.__course
	def getdivision(self):
		return self.__division
	def getrole(self):
		return self.__roll_no
	def getmarks(self):
		return self.__marks
	def __repr__(self):
		return "\nName" +self.__name+ "\nAddress" + self.__address + "\nDOC " + self.__dob + "\nRollNO" + str(self.__roll_no)
		
		
	def updateaddr(self, add):
		self.__adress =address
	def updatemarks(self, subject, marks ):
		self.__marks[subject] =marks 
	def updatecourse(self, course):
		self.__course =course
		
	def updatedivision(self, division):
		self.__division = division
		
class studentmanager:

	def __init__(self,no_of_student):
		self.__no_of_students= no_of_student
		self.__enrolled_student = dict()
		self.__suspended_students = dict()
	
	def addstudent(self, name, address, dob, course, division):
		st = student(name, address, dob, course, division)
		self.__enrolled_student[st.getrole() ] =st
	
	def suspentstudent(self, rollno):
		if rollno in self.__suspended_students:
			pass
		elif rollno in self.__enrolled_student:
			
			st = self.__enrolled_student.pop(rollno)
			self.__suspended_students[rollno] = st
		else: 
			return False
		return True
	def getstudent(self):
		return self.__enrolled_student
		
	def updatemarks(self, rollno, subject, marks):
		if rollno in self.__enrolled_student:	
			self.__enrolled_student[rollno].updatemarks(rollno, subject, marks)
			return True
		return False
	def getstudentmarks(self, rollno):
		return self.__enrolled_student[rollno] ==getmarks()
		
		

def unitteststuent():

	stud = student("student1" , "Pune", "12-12-2012", "10th", "A")
	stud.updatemarks("engish", 50)
	stud.updatecourse("python")
	print ("Marks : ", stud.getmarks())
	print ("Name: " , stud.getName())
	print ("Address: " , stud.getAddress())
	print ("DOB:" ,stud.getdob())
	print ("Course: ", stud.getcource())
	print ("Division :" ,stud.getdivision())
	print ("Role No : ", stud.getrole())
	stud1 = student("student2" , "Pune", "1-1-2012", "11th", "B")
	print ("Name: " , stud1.getName())
	print ("Address: " , stud1.getAddress())
	print ("DOB:" ,stud1.getdob())
	print ("Course: ", stud1.getcource())
	print ("Division :" ,stud1.getdivision())
	print ("Role No : ", stud1.getrole())
	

def unittest_stud_mgmt():
	
	s= studentmanager(50)
	s.addstudent("student1" , "Pune", "12-12-2012", "10th", "A")
	s.addstudent("student2" , "Pune", "1-1-2012", "11th", "B")
	s.addstudent("student3" , "Pune", "2-2-2012", "11th", "B")
	student =s.getstudent()

	for st in student:
		print ("\nAfter adding students")
		print (student [st])
	
	s.suspentstudent(1)
	
	for st in student:
		print ("\nAfter removing students")
		print (student [st])
	s.getstudentmarks(3)
	s.updatemarks("2", "Python", "40")
	s.getstudentmarks("2")
	

if __name__=="__main__":
	#unitteststuent()
	unittest_stud_mgmt()
		