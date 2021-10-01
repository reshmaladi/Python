#!/usr/bin/python

class Person:
	def __init__(self, name, address, dob, mobileno, gender, adharno):
		self.name = name
		self.address =address
		self.dob = dob
		self.mobileno= mobileno
		self.adharno= adharno
		self.gender = gender
		
	def updatename(self, name):
		self.name =name
	def updateaddress(self, address):
		self.address = address
	def updateadhar(self, adharno):
		self.adharno= adharno
	def mobileno(self,mobileno):
		self.mobilno = mobileno
		
class Employee:
	auto_emp_no = 1
	def __init__(self, name, address, dob, mobileno,gender, adharno, dept, desig, salary, projectname, location, email):
		self.__emp_no = Employee.auto_emp_no
		Employee.auto_emp_no += 1
		emp = Person(name,address, dob, mobileno,gender, adharno)
		self.name = emp.name
		self.address =emp.address
		self.dob =emp.dob
		self.gender =emp.gender
		self.adharno = emp.adharno
		self.dept = dept
		self.desig = desig
		self.salary = salary
		self.projectname = projectname
		self.location = location
		self.email= email
				
	def getempid(self):
		return self.__emp_no
	def getempname(self):
		return emp.name
	def getempadd(self):
		return emp.address
		
	def __repr__(self):
		return "Name:"+self.name+"\nAddress:"+self.address+"\nDOB:"+self.dob+"\nEmp ID:"+str(self.__emp_no)
		
class EmpoyeeManager:
	def __init__(self, noOfEmpoyees):
		self.__no_of_empoyees = noOfEmpoyees
		self.__active_employees = dict()
		self.__resgned_employees = dict()
		
	def AddEmployee(self, name, address, dob, mobileno,gender, adharno, dept, desig, salary, projectname, location, email):
		addemp = Employee(name, address, dob, mobileno,gender, adharno, dept, desig, salary, projectname, location, email)
		self.__active_employees[addemp.getempid()] = addemp
	
	def getActiveEmp(self):
		return self.__active_employees 
		
def main():
	n = 10 # accept from user
	sm = EmpoyeeManager(n)
	sm.AddEmployee("R1", "Pune" , "1-1-2010", "987654321","F", "1234", "it", "snr dev", "5lac", "abc", "pune", "abc@abc.com")
	empdetails= sm.getActiveEmp()
	print (empdetails)
if __name__ == "__main__":
    main()
	
	
'''
    
	def getresignedemp(self):
		return self.__resigned
		
	def getactive(self):
		return self.__active
		
	def addemp(self):
		emp = Person(name, dob, address,mobileno, gender, adharno)
		
		
	def __repr__(self):
        return "Name:"+self.__name+"\nAddress:"+self.__address+"\nDOB:"+self.__dob+"\nRoll No:"+str(self.__roll_no)
'''

		