#!C:\Python34
'''
only stack not
global interpreter lock  : mutex 
semaphore  

thread >> have stack >> 
shares text (instratuctions) region 
uses data from processes 
'''

import threading

def worker():
    """thread worker function"""
    print ("Worker")

if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()

if we inherited class then we have to wirte run method if run method is not written then we have to clal constructor and there should be worker metheod written .
