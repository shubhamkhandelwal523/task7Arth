#!/bin/bash
import os
import getpass
os.system("tput setaf 3")
print("\t 8888888888888888888888888888888888888888")
os.system("tput setaf 7")
os.system("figlet -f digital\t\t HEY !! Welcome TO MY MENU")
os.system("tput setaf 3")
print("\t 8888888888888888888888888888888888888888")
os.system("tput setaf 4")
passwd = getpass.getpass("Enter Your Password :")

apass = "redhat"

if passwd != apass:
    print("Authentication Incorrect")
    exit()

os.system("tput setaf 7")
print("Where You Would Like To Perform Your Job (local) :" , end='')
location = input()
print(location)

if location == "remote":
    remoteIP = input("Enter Your IP :")
os.system("tput setaf 3")
os.system("figlet \t\t HADOOP !")
os.system("tput setaf 5")
print("IMPORTANT:- BEFORE RUN ANY COMMAND YOU HAVE TO START THE NAMENODE AND DATANODE FIRST") 
os.system("tput setaf 1")
while True:
	print("""
		Press 1: To see date
		Press 2: To see the connected harddisk 
		Press 3: To Download Hadoop and java software use link
		Press 4: To install hadoop s/w 
		Press 5: To install java s/w
		Press 6: To Create A physical volumes
		Press 7: TO see a physical volume(PV)
		Press 8: TO create a Volume group
		Press 9: TO see the Volume group(VG)
		Press 10: To create Logical Volume i.e. LVM
		Press 11:TO see The Logical volume
		Press 12:To Format the Logical Volume
		Press 13:For mounting the partition
		Press 14:TO extend/shrink the size of LVM
		Press 15:Reformat the size of extended part
		Press 16:To check the report of datanode
		Press 17:To exit
		""")
	print("Press any no. that you want to perform :" , end='')
	ch = input()
	print(ch)

	if location == "local":
		if int(ch) == 1:
			os.system("tput setaf 7")
			os.system("date")
			os.system("clear")
		elif int(ch) == 2:
			os.system("clear")
			os.system("tput setaf 7")
			os.system("fdisk -l")
		elif int(ch) == 3:
			print("Use below link to download the software")
			os.system("tput setaf 7")
			print("https://drive.google.com/drive/u/0/folders/1NowQFq4oMpqX3SYMp-L0GM8oi-2SwJSM")
			os.system("clear")
		elif int(ch) == 4:
			print("Installing Hadoop")
			os.system("tput setaf 7")
			os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
			os.system("clear")
		elif int(ch) == 5:
			print("Installing Java(jdk)")
			os.system("tput setaf 7")
			os.system("rpm -ivh jdk-8u171-linux-x64.rpm  --force")
			os.system("clear")
		elif int(ch) == 6:
			print("To create A physical volume give name of attached harddisk 1 :" , end = '')
			pv_name1 = input()
			os.system("tput setaf 6")
			print("To create A physical volume give name of attached harddisk 2 :" , end = '')
			pv_name2 = input()
			os.system("pvcreate {} {}".format(pv_name1,pv_name2))
			os.system("clear")
		elif int(ch) == 7:
			print("physical volume")
			os.system("tput setaf 7")
			os.system("pvdisplay")
			os.system("clear")
		elif int(ch) == 8:
			print(" Give Name to VG:" ,end = '')
			vg_name = input()
			os.system("tput setaf 6")
			print("Enter PV Harddisk names:" , end ='')
			pv_names = input()
			os.system("tput setaf 7")
			os.system("vgcreate {} {} ".format(vg_name,pv_names))
			os.system("clear")
		elif int(ch) == 9:
			print("Volume group")
			os.system("tput setaf 7")
			os.system("vgdisplay")
		elif int(ch) == 10:
			print("Give Size : " , end= '')
			os.system("tput setaf 7")
			size_no = input()
			print("Give lv_name :" , end= '')
			name = input()
			print("Give vg_name that you given In VG :" , end= '')
			vg = input()
			os.system("lvcreate --size {} --name {} {}" .format(size_no,name,vg))
			os.system("clear")
		elif int(ch) == 11:
			print("Logical volume")
			os.system("tput setaf 7")
			os.system("lvdisplay")
		elif int(ch) == 12:
			print("Give LV path :" ,end = '')
			os.system("tput setaf 7")
			lv_path = input()
			os.system("mkfs.ext4 {} " .format(lv_path))
		elif int(ch) == 13:
			print("Mounting .. " , end = '')
			print("\n Give LV_PATH :" , end = '')
			path = input()
			os.system("tput setaf 6")
			print("Give folder name where you want to mount :" , end = '')
			file_name = input()
			os.system("mount {} {} ". format(path,file_name))
		elif int(ch) == 14:
			print("Give Size : " , end= '')
			os.system("tput setaf 7")
			size_no = input()
			print("Give lv_path:" , end= '')
			name = input()
			os.system("lvextend --size {} {}" .format(size_no,name))
			os.system("clear")
			print("\n After using the Press 14 use Press 11 to see LV display", end ='')
		elif int(ch) ==15:
			print("Resizing the partition ",end = '')
			os.system("tput setaf 5")
			print("Give LV_path:" , end = '')
			name = input()
			os.system("resize2fs {} ".format(name))
		elif int(ch) == 16:
			print("checking datanode report.." ,end = '')
			os.system("tput setaf 7")
			os.system("hadoop dfsadmin -report")
		elif int(ch) == 17:
			print("Exiting" ,end = '')
			os.system("tput setaf 7")
			os.system("hadoop dfsadmin -report")

			
	else:
		print("Option Not Supported")
		input("Enter To Continue......")
		os.system("clear")

			
			
			
			


