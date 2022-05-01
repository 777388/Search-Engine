import os
import socket
from threading import Thread
from time import sleep
def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)[0]
     except socket.herror:
         return None
def threadhead(arg):
	for j in range(arg):
		for i in range(0, 255, 1):
			for n in range (0, 255, 1):
				for k in range (0, 255, 1):
					for d in range (0, 255, 1):
						h = str(str(i)+"."+str(n)+"."+str(k)+"."+str(d))
						g = str("\r"+h+"\r")
						f = "curl -s -I "+h+" >> trash.txt"
						t = os.system(f)
						p = "python3 Sublist3r/sublist3r.py -d "+str(lookup(h))+" >> "+str(lookup(h))+".txt"
						q = "wsl cat "+str(lookup(h))+".txt | gau --threads 5 --o "+str(lookup(h))+".txt"
						if lookup(h) != None: 
							print(h+str(lookup(h)))
							o = os.system(p)
							m = os.system(q)
						else:
							print(g, end='', flush=True)
				
if __name__ == "__main__":
	thread = Thread(target = threadhead, args=(1, ))
	thread.start()
	thread.join()
	print("finished")