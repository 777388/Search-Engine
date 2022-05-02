import os
import socket
from threading import Thread
from time import sleep
import sys

def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)[0]
     except socket.herror:
         return None

def threadhead(arg):
	for i in range(arg, arg+1, 1):
		for n in range (0, 255, 1):
			for k in range (0, 255, 1):
				for d in range (0, 255, 1):
					h = str(str(i)+"."+str(n)+"."+str(k)+"."+str(d))
					g = str("\r"+h+" \r")
					if lookup(h) != None: 
						with open('searchengine.txt', 'a') as hi:
							print(str(lookup(h))+" \r", file=hi)
					else:
						print(g, end='', flush=True)
				

if __name__ == "__main__":
	threads = []
	for x in range(0, 255, 1):
		thread = Thread(target = threadhead, args=(x, ))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
	with open('searchengine.txt')as thing:
		for line in thing:
			am = ("amass intel -d "+line.rstrip()+" -whois -o servers.txt")
			heh = os.system(am)
	with open('servers.txt') as that:
		for line in that:
			p = ("python3 Sublist3r/sublist3r.py -d "+line.rstrip()+" -o "+line.rstrip())
			o = os.system(p)
			q = ("wsl cat "+line.rstrip()+"| gau --threads 5 -o "+line.rstrip()+"1.txt")
			op = os.system(q)
