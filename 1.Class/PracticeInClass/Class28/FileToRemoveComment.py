#!C:\Python34
import re

def main():
	fd = open( "C:\\1.Class\\PracticeInClass\\Class28\\audio.conf")
	data = fd.read()
	fd.close()
	ob = re.sub(re.compile("'''.*?'''", re.DOTALL ) ,"" ,data)
	ob1 = re.sub(re.compile("\""".*?\"""",re.DOTALL  ) ,"" ,ob)
	ob2 = re.sub(re.compile("#.*", re.MULTILINE), "", ob1)
	print (ob2)
	
	fd_w = open("C:\\1.Class\\PracticeInClass\\Class28\\audio_new.conf", "w")
	fd_w.write(ob2)
	fd_w.close()

if __name__ == "__main__":
    main()

