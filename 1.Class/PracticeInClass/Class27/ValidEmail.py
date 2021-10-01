#!C:\Python34
import re
EmailIDs = []
while True :
	EmailID = input("Enter list of email ID with comma separated, to stop enter n")
	if ( EmailID == "n"):
		break
	else :
		EmailIDs.append(EmailID)
for emailid in EmailIDs:
	m = re.match("(\w+)@(\w+)\.(\w+)", emailid)
	if m != "None":
		print (emailid , "Valid")
		
	else:
		print (emailid , "Not Valid")
    
	

