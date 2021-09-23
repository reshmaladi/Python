import os 
size = 0

folderpath= 'C:\\PrepareNow\\1.Format\\'

for path, dir , files in os.walk(folderpath):
	for f in files:
		fp = os.path.join(folderpath, f)
		print(fp)
		size +=os.path.getsize(fp)
print(size)