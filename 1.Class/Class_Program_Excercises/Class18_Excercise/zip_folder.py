#!C:\Python34
import shutil 

def zip_file(path, folder):
	shutil.make_archive('myarchive', 'zip', path , folder)


def main():
	folder= input("Enter folder: ")
	path = input("Enter path for zip" )
	zip_file(path, folder)


if __name__=="__main__":
	main()