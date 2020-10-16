from os import system as sys

#option18 Docker Operations
def what_docker(x):
	if x == 1:
		sys('sudo docker images')
		print()

	elif x == 2:
		os_name = input("Enter os_name : ")
		image_name = input("Enter image_name : ")
		sys("sudo docker run -dit --name {} {}".format(os_name,image_name))
		print()

	elif x == 3:
		sys('sudo docker ps -a')
		print()

	elif x == 4:
		os_name = input("Enter os_name which you want to stop : ")
		sys('sudo docker rm -f {}'.format(os_name))
		print()

	elif x == 5:
		image_name = input("Enter image_name : ")
		tag = input("Enter tag_name : ")
		sys('sudo docker pull {}:{}'.format(image_name,tag))
		print()

	elif x == 6:
		sys('sudo docker network ls')
		print()

	elif x == 7:
		os_name = input("Enter os_name : ")
		sys('sudo docker exec -it {} bash'.format(os_name))
		print()
	
	elif x == 8:
		sys("sudo systemctl status docker")
		print()
	
	elif x == 9:
		system("sudo systemctl start docker")
		print()
	elif x == 10:
		system("sudo docker rm -f $(docker ps -a -q)")
		print()
	elif x == 11:
		image_name = input("Enter image_name : ")
		sys('sudo docker image rm -f {}'.format(image_name))
		print()
	else :
		print("Invalid input !!!")
	return
