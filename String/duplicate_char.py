#!C:\Python34
import pdb; pdb.set_trace()
st = "tutorialspoint"
dup = {}
for el in st:
	if el in dup:
		dup[el] += 1
	else: dup[el] =1

for e, val in dup.items():
	if val >1:
		print(e, val)
