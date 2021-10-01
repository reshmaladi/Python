#!/usr/bin/python

'''
try:
	a +=10
except NameError as e:
	print (e)


'''



try:
	num = eval(input("Numerator:\t"))
	den = eval(input("Denominator:\t"))
	result = num/den
	

except ZeroDivisionError as e:
	print("Zero Division Error", e)
	
except Exception as e:
	print ("Execute if any type of execption occures" , e)

else: 
	print ("Else block: execute when execption does not occures")
finally:
	print ("Finally block: Executed always")