#!/bin/bash

if [[ $# -gt 5 ]]; then

echo -e "Please, provide me with no more than five words, i.e. my arguments, to search for. Try again with no more than five words."

echo -e "That said, do realize that 'snap find ...' works with only one argument... Unless, my dear user, you use quotation marks, likeso:\n"

echo -e "snap find 'racket clone tetris'\n"

echo -e "Other than that, if you would not to use CLI, consider looking for packages online:\n"

echo -e "https://www.archlinux.org/packages/\n" 

echo -e "https://www.debian.org/distrib/packages\n" 

echo -e "https://packages.ubuntu.com/\n"

echo -e "https://snapcraft.io/store\n" && exit

fi


if [[ -d /etc/pacman.d ]]; then

echo -e "\n Methinks we are dealing with an Arch-based system. The results of 'pacman -Ss ${1} ${2} ${3} ${4} ${5}':\n"

pacman -Ss $1 $2 $3 $4 $5

read -p "Do you wish to search for packages online instead? Enter Y or N." answer

	if [[ $answer == 'y' ]]; then
	xdg-open https://www.archlinux.org/packages/

	fi

elif [[ -d /etc/apt ]]; then

echo -e "Methinks we are dealing with a Debian-based system. The results of 'apt-cache search ${1} ${2} ${3} ${4} ${5}':\n"

apt-cache search $1 $2 $3 $4 $5 || echo -e "No packages were found with for apt tool.\n" 

echo -e "\nThe results of 'snap find ${1} ${2} ${3} ${4} ${5}':\n"

snap find "$1 $2 $3 $4 $5"

fi

exit

# snap find does not work without quotation marks when dealing with multiple arguments
#https://snapcraft.io/docs/getting-started
