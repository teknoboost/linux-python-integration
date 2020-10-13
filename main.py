from os import system as sys
import getpass
from termcolor import colored
from python_operations import what_py
from docker_operations_all import what_docker
import smtplib

#code for banner and designs
print(sys("figlet LINUXPY"))
print()
print()

#read password from file
f = open("password.txt",'r')
password = f.read()
password = password[0:len(password)-1]

#password setup
x = getpass.getpass("Enter Your Password : ")

if x==password:
	print(colored("LogIn Successfull !","red"))
	print()
else :
	print(colored("Password is Incorrect !","red"))

#menu-bar
first_time = True
if x == password:
	while True:
		if first_time:
			all_operations_display()
			first_time = False
		else:
			print(colored("Enter \'all\' to see complete operations list.\nor\nEnter option directly if you know the operation number\n","blue"))
		choice = (input("Enter Your Choice : "))
		if choice == "all":
			all_operations_display()
			choice = (input("Enter Your Choice : "))
		try:	
			choice = int(choice)
		except Exception as e:
			print(colored("\nPlease enter numbers only.","red"))

		if(choice == 1):
			sys("sudo su")
			print()

		elif choice == 2:
			sys("date")
			print()

		elif choice == 3:
			sys("bc")
			print()

		elif choice == 4:
			print("Enter user name : ",end="")
			create_user = input()
			sys("useradd {}".format(create_user))
			print()

		elif choice == 5:
			print("Enter software name : ",end="")
			software_name=input()
			sys("sudo apt-get install {}".format(software_name))
			print()

		elif choice == 6:
			sys("gnome-terminal")
			print()

		elif choice == 7:
			sys("subl new.txt") #open a new txt file in sublime text editor
			print()

		elif choice ==  8:
			sys("sudo apt-get update")
			print()

		elif choice == 9:
			print('''What you wanna do : 
1 :launch python 
2 :Create or edit a python code 
3 :Run your python file
4 :Install a package''')
			X = int(input("Enter your choice :"))
			what_py(X)

		elif choice == 10:
			print("Enter Website or IP : ",end="")
			website = input()
			sys("nmap {}".format(website))
			print()

		elif choice == 11:
			sys("ifconfig")
			print()

		elif choice == 12:
			print("Enter Website or IP : ",end="")
			website = input()
			sys("ping {}".format(website))
			print()

		elif choice == 13:
			sys("sudo apt-get install apache2")
			print()

		elif choice == 14:
			print("enter banner name : ",end="")
			banner_name = input()
			sys("figlet {}".format(banner_name))
			print()

		elif choice==15:
			print("enter command : ",end="")
			new_cmd = input()
			sys("{}".format(new_cmd))
			print()

		elif choice == 16:
			sys("google-chrome")
			print()

		elif choice == 17:
			print("Enter name : ",end="")
			s_file = input()
			sys("which {}".format(s_file))
			print()

		elif choice == 18:
			print('''What you wanna do : 
1 : to see images 
2 : to launch container
3 : to see running containers
4 : to stop os/container
5 : to pull image from docker hub
6 : to see network list
7 : to execute container running in background
8 : to check docker status 
9 : to start the docker 
''')
			x = int(input("Enter your choice :"))
			what_docker(x)

		elif choice == 19:
			print("Enter website name : ",end="")
			website = input()
			sys("google-chrome {}".format(website))
			print()
		elif choice == 20:
			sender_email = input(str("Enter your email :"))
			rec_email = input(str("Enter receiver_email :"))
			message = input("Enter your message : ")
			password = getpass.getpass("Enter Your Password : ")
			server = smtplib.SMTP('smtp.gmail.com',587)
			server.ehlo()
			server.starttls()
			server.login(sender_email,password)
			print("LogIn Successfull")
			server.sendmail(sender_email,rec_email,message)
			print("Your Email has been sent to : ",rec_email)
		
		elif choice == 21:
			dir_name = input("Enter name of Directory")
			sys("mkdir {}".format(dir_name))
      
                elif choice == 22:
			sys("firefox")
			print()
		
		elif choice == 23:
			sys("free -m")
		
		elif choice == 24:
			sys("df -h")
			
		elif choice == 25:
			sys("exit")
			print(colored("Thanks For Using.","red"))
			break
		else :
			print(colored("Invalid Choice.Please re-enter.\n","red"))
