#!/usr/bin/python
import sys
import random

try:
	import nmap # import nmap.py module
	print "nmap imported... let's begin :-)"
except ImportError:
	print "nmap not installed, try something else..."
pass

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
PURPLE = "\033[0;35m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

sys.stdout.write(GREEN)
loading = ["Loading...","Mining Bitcoin","Entering the Matrix","Mining shitcoin"]

def title():

    print('|---------------------------------------|')
    print('|---------------------------------------|')
    print('|---------------------------------------|')
    print('|-------------n0f4x Scanner-------------|')
    print('|---------------------------------------|')
    print('|---------------------------------------|')
    print('|---------------------------------------|')
	                                                                                    
    return random.choice(loading)

def scanNet(ip, port, arg):

	sys.stdout.write(BLUE)
	nm = nmap.PortScanner() # instantiate nmap.PortScanner object

	#nm.scan('192.168.1.84', '22-443') # scan host 127.0.0.1, ports from 22 to 443
	nm.scan(hosts= ip, ports=port, arguments=arg)

	
	
	name = str(nm[ip].hostnames())
	cleanName = name.replace("{'type': 'PTR', 'name': '","")
	cleanName2 = cleanName.replace("'}","")
	print('|---------------------------------------|')
	print('| Hostname: ' + cleanName2)

	
	print('|---------------------------------------|')
	print('| IP ' + ip +' is: ' + nm[ip].state())
	

	for proto in nm[ip].all_protocols():
            print('|---------------------------------------|')
            print('| Protocol : %s' % proto)

  	


  	print('|---------------------------------------|')
	print('| Open ports: ' +str(nm[ip].all_tcp()))
	print('|---------------------------------------|')


	return ('Complete')



#Printing on terminal begins here 
print title()

#take input before scanning
inputIP = raw_input("Enter Target IP: ")
inputPort = raw_input("Enter Port to look at(i.e. 22 or 22-443): ")
inputArg = raw_input("Enter nmap arg(i.e. -sC): ")
print('Loading...')

#output scan - passes input to def
print scanNet(inputIP, inputPort, inputArg)

#change colour for next chapter
sys.stdout.write(GREEN)

#--------------------Initiate next phase-----------------------
inputNextStage = raw_input("Attack "+inputIP+" ? [Y/N] ")
inputMethod = raw_input("|dos|arp|ssh| ?")
print(random.choice(loading))

def attack(choice,method):
	if(choice.lower()=="y"):
		print('|---------------------------------------|')
		print('yes attack')
		print('|---------------------------------------|')
		if(method.lower()=="dos"):
			print('skid')
			print('|---------------------------------------|')

	elif():
		print('no attack')	


print attack(inputNextStage,inputMethod)

sys.exit()



