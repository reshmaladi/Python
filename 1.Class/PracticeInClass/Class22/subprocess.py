#!C:\Python34
import subprocess

def foo():
	print ("Executed..")

proc = subprocess.Popen(['echo', '"to stdout"'], stdout=subprocess.PIPE )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)
#subprocess.Popen(["echo" , "to the stdout"], preexce_fn =f00)
