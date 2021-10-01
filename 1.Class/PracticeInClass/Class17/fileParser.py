#!C:\Python3
import configparser as CFT
def ParseConfigFile(cfg_file_name):
	parser = CFT.ConfigParser()
	parser.read(cfg_file_name)
	print ("sections are : ", parser.sections())
	print ("Options are :", parser.options("First"))
	#print (parser.get("First", "ip"))


def main():
	cfg_file_name = "C:\\1.Class\\Class_Program_Excercises\\Class16_Excercise\\config.cfg"
	Parsed_Configurations = ParseConfigFile(cfg_file_name)
	ParseConfigFile(cfg_file_name)

if __name__=="__main__":
	main()
	
	