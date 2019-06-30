#!/usr/bin/python
import sys
import os
import random

try:
	import nmap # import nmap.py module
	print "Nmap imported. Let's begin."
except ImportError:
	print "Nmap not installed. Try pip install python-nmap or something else."
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
loading = ["Loading...","Generating Electricity...","Mining Bitcoin...","Entering the Matrix...","Mining shitcoin..."]

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

#logic for netdiscover input. Spawns a shell process
def netdiscover(str):	
	if str.lower() == "y":
		list = os.system("sudo netdiscover")
		print(list)
	if str.lower() == "?":
		print ("netdiscover scans Local Net for devices, run 'sudo apt-get install netdiscover' to install it")



#Printing on terminal begins here 
print title()

#netdiscover
inputDiscover = raw_input("Would you like to run netdiscover in shell? [Y/N/?] PRESS CTRL+C TO CONTINUE WHEN RUNNING NETDISCOVER: ")
netdiscover(inputDiscover)

#netdiscover python
inputPyDis = raw_input("Would you like to run netdiscover in Python? [Y/N/?]")
netDiscover.netdiscoverPy(inputPyDis)

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
inputMethod = raw_input("arp or ssh| ?")
print(random.choice(loading))

def attack(choice,method):
	if(choice.lower()=="y"):
		print('|---------------------------------------|')
		print('yes attack')
		print('|---------------------------------------|')
		if(method.lower()=="arp"):
			list = os.system("sudo ettercap -M " + inputIP)
			print(list)
			print('|---------------------------------------|')

		if(method.lower()=="ssh"):
			list = os.system("sudo ssh " + inputIP)
			print(list)
			print('|---------------------------------------|')
	if(choice.lower()=="n"):
		print('no attack')	


print attack(inputNextStage,inputMethod)

sys.exit()



