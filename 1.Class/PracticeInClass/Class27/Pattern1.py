#!C:\Python34
import re
#match_it = re.finditer("(\w+)\.(\w+)", "jeetendra$tig.er$tig.er$Lion$tig.er")
match_it = re.finditer("(\w+)@(\w+)\.(\w+)", "resh@test.com, admin@test.com, sds@sds")
for match in match_it:
	print (match.start(), match.end(), match.group(0),match.group(1), match.group(2))
	
	
	