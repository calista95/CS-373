import psutil
import os
import threading
import subprocess

cont = True
while cont == True:

    print("Here are your options:")
    print("1. Enumerate all the running processes.")
    print("2. List all the running threads within process boundary.")
    print("3. Enumerate all the loaded modules within the processes.")
    print("4. Show all the executable pages within the processes.")
    print("5. Read memory.")
    print("6. Exit the program.")
    choice = int(input("Type in a number:"))

    if (choice ==1):
        #Enumerate all the running processes
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
		except psutil.NoSuchProcess:
			pass
		else:
			print(pinfo)
	raw_input("Press any character to continue.")
    elif (choice ==2):
        #List all running threads w/in process boundary
	pid = input("Enter the PID of a process you want to see running threads for:")
	#pstree $PID
	if (psutil.pid_exists(pid) == True):
		p = psutil.Process(pid)
		array = p.threads()
		for x in array:
			print x
	else:
		print("Specified PID is not valid")
	raw_input("Press any character to continue.")
    elif (choice ==3):
        #Enumerate all loaded modules within the processes
	pid = input("Enter the PID of a process you want to see loaded modules for:")
	if (psutil.pid_exists(pid) == True):
		p = psutil.Process(pid)
		array = p.connections()
		for x in array:
			print x
	else:
		print("Specified PID is not valid")
	raw_input("Press any character to continue.")
    elif (choice ==4):
        #Show all executable pages within the processes
	pid = input("Enter the PID of a process you want to see executable pages for:")
	if (psutil.pid_exists(pid) == True):
		p = psutil.Process(pid)
		for x in p.open_files():
			print x
	else:
		print("Specified PID is not valid")
	raw_input("Press any character to continue.")
    elif (choice ==5):
        #Read memory
	pid = input("Enter the PID of a process you want to see the memory of.")
	if (psutil.pid_exists(pid) == True):
		p = psutil.Process(pid)
		print p.memory_maps()
	else:
		print("Specified PID is not valid")
	raw_input("Press any character to continue.")
    elif (choice == 6):
        cont = False
