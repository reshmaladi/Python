#!C:\Python34
import hashlib 

in_file = "C:\\Users\\reshma.ladi\\Documents\\GitHub\\Python\\File_handling\\temp_file.txt"
out_file = "C:\\Users\\reshma.ladi\\Documents\\GitHub\\Python\\File_handling\\removed_dup.txt"

fin = open(in_file, "r")
fout = open(out_file, "w")

line_hash = set()

for line in fin:
	print (line)
	hashval = hashlib.md5(line.rstrip().unicode("utf-8")).hexdigest()
	print (line)
	if hashval not in hash_line:
		fout.write(line)
		line_hash.add(hashval)
fout.close()
fin.close()