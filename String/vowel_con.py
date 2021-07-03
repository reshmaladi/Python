#!C:\Python34
st= "absdauoi"
con_v , con_c = 0,0
for ele in st:
	if ele in ["a", "e", "i", "o", "u"]:
		con_v += 1
	else : 
		con_c += 1
print ("Con, volwel", con_c, con_v)
