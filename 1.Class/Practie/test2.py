#!C:\Python34
#Program to replace "not bad" string with "good"
a  = input ("Enter the sentence ")
not_index = a.find("not")
if not_index != -1:
    bad_index =a.find("bad")
    if bad_index != -1 and bad_index > not_index:
		
        result = a [: not_index]
        result += 'good' 
        result += a[ bad_index +3 :]
print (result)			

