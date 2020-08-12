#!/bin/bash

echo -e "Good morrow, my dear user. Before we start doing anything to your drive let me show you your partition table:\n"

sudo fdisk -l|grep /dev/sd


echo -e "\n\n\nType 'lsblk', 'df -h' or 'sudo fdisk -l|grep /dev/sd' to for more information about you partition table."

echo -e "\nTo exit the script at any time press Ctrl^C of Ctrl^D."

echo -e "\nWhat is the path to the USB drive in question?\n"

read path

echo -e "\nWhat would you like to do with the $path drive:\n"

echo -e "1. Erase all signatures from your drive with 'wipefs', which is the first step in recovering a bootable USB.\n"

echo -e "2. Further continue the process of recovery by creating a primary partition.\n"

echo -e "3. Over-write all information blocks in your flash drive with zeros. This would take longer then the first and second tasks altogether. Going for it is usually not needed for the sake of recovering a bootable USB or creating one."  

echo -e "\n4. Create a bootable drive ?\n"

echo -e "   Please type 1, 2, 3 or 4 and press Enter."

read I_would

if [[ $I_would == 1 ]]; then

sudo nice -19 wipefs --all $path

elif [[ $I_would == 2 ]]; then

	echo -e "We are going to use cfdisk to acomplish this goal. Select 'DOS partition type', 'primary', and 'write' instead of 'quit' in the consecutive steps.\n"
	
	echo -e "Type 'y' if you are ready to proceed with cfdisk."
	
	read proceed

	if [[ $proceed == y ]]; then
		sudo cfdisk $path

	else 
		echo -e "Next time type 'y' if you are ready to proceed with cfdisk. I'm going to exit the script now."
		exit

	fi
		
	

elif [[ $I_would == 3 ]]; then

	sudo nice -19 dd if=/dev/zero of=$path status=progress

elif [[ $I_would == 4 ]]; then

echo -e "What is the path to your .iso file? If the image is in your current directory, just the filename will do. If it is not in you current directory, give me the full path, without substituting '~' for your home directory."

read iso_path

sudo nice -19 dd if=$iso_path of=$path bs=4M status=progress && sync

echo -e "Remember to safely remove the USB from its port, e.g. by running 'umount ${path}1' .\n\n\nShare you tools and solutions. Fare you well."

exit


else

	echo -e "Choose only between 1., 2., 3. and 4."

	exit

fi

echo -e "Something went wrong."

exit
