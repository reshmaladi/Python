#!C:\Python34
import threading

def worker():
    """thread worker function"""
    print ("Worker")

if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()

