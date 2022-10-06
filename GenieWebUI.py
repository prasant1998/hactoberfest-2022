#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

cmd=cgi.FieldStorage()
op=cmd.getvalue('q')


if ("cent" in op ) and ('7' in op):
	print("Cent OS 7 Container is running...")
	print(sp.getoutput("sudo docker run -dit centos:7"))

elif ("ubuntu" in op):
	print("Ubuntu Latest Container is running...")
	print(sp.getoutput("sudo docker run -dit ubuntu:latest"))
	
elif ("ip" in op):
	print("Your IP Address is: ")
	print(sp.getoutput("sudo ifconfig"))
elif ("shadow" in op):
	print("Your Shadow File: ")
	print(sp.getoutput("sudo cat /etc/shadow"))
elif ("who" in op):
	print(" You Are: ")
	print(sp.getoutput("sudo whoami"))
elif ("directory" in op):
	print("Your Current Working Directory is: ")
	print(sp.getoutput("sudo pwd"))
elif ("memory" in op) or ("ram" in op):
	print("Here is Your Memory Details: ")
	print(sp.getoutput("sudo free -t"))
elif ("cpu" in op) or ("processor" in op):
	print("Here is your CPU details: ")
	print(sp.getoutput("sudo lscpu"))
elif ("docker" in op) and ("version" in op):
	print("Installed Docker Details: ")
	print(sp.getoutput("sudo docker version"))
elif ("boot" in op):
	print("Here is Your Server boot log: ")
	print(sp.getoutput("sudo dmesg"))
elif ("calender" in op):
	print("Here is Your calender: ")
	print(sp.getoutput("sudo cal"))
elif (("delete" in op) or ("stop" in op)) and ("container" in op):
	print("All Docker Containers are cleared.")
	print(sp.getoutput("sudo docker rm -f $(sudo docker container ls -a -q)"))
elif ("show" in op) and (("containers" in op) or ("docker" in op)):
	print("Here is your all the Docker Containers Running List: ")
	print(sp.getoutput("sudo docker container ls")) 

else:
	print("Sorry Your Query Can't be Completed Right Now...")
