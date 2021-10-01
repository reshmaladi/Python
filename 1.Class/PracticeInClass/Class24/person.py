#!/usr/bin/python
class Person:
    def __init__(self, name, address, dob):
        self.__name = name
        self.__address = address
        self.__dob = dob
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getDOB(self):
        return self.__dob
    def updateAddress(self, address):
        self.__address = address
    def __repr__(self):
        return "Name:"+self.__name+"\nAddress:"+self.__address+"\nDOB:"+self.__dob+"\nRoll No:"+str(self.__roll_no)