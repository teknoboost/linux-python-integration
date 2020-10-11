from os import system as sys

#Option9 Python Operations
def what_py(x):
	if x == 1:
		sys('python3')
	elif x == 2 :
		fn = input("Enter file name to start writing code :")
		sys("subl {}".format(fn)) #sublime text editor
	elif x == 3 :
		pth = input("Enter name of the file you want to run :")
		sys("python3 {}".format(pth))
	elif x == 4 :
		nm = input ("Enter package name :")
		sys("pip3 install {}".format(nm))
	else :
		print("Invalid input !!!")
	return
