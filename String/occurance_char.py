#!C:\Python34

st ="happyprogrampppming"
ch = "p"

occ = {}

for ele in st:
	if ele not in occ:
		occ[ele] =1
	else: occ[ele] += 1 
for e, k in occ.items():
	if ch == e :
		print (k)