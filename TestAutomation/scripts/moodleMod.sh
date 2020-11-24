#!/bin/bash

#
# moodleMod.sh
# scripts
# 
# New-Leaf
# lukem1
# 23 November 2020
#

#
# This script automates several common procedures used to setup, clean, and manipulate the moodle project.
#

usage="Usage: ./scripts/moodleMod.sh <action>
Actions:
  clone  - clone the moodle project into ./project/moodle
  delete - delete ./project/moodle
  inject - inject predefined faults into moodle
  reset  - clean and reset moodle to its original state"
  
path="./project/moodle"
faults="./project/faults"

if [[ -n "$1" && $# -eq 1 && "$0" == "./scripts/moodleMod.sh" ]]
then

	if [ $1 == "clone" ]
	then
		if [ ! -d "$path" ]
		then
			mkdir $path
			git clone -b MOODLE_39_STABLE git://git.moodle.org/moodle.git $path
		else
			echo "Error: $path already exists!"
		fi
	elif [ $1 == "delete" ]
	then
		if [ -d "$path" ]
		then
			read -p "Confirm the deletion of $path (y/n)? : " -n 1 -r
			if [[ $REPLY =~ ^[Yy]$ ]]
			then
				echo -e "\nDeleting $path..."
				rm -rf $path
			else
				echo -e "\nCanceled."
			fi
		else
			echo "Error: $path does not exist!"
		fi
	elif [ $1 == "inject" ]
	then
		if [[ -d "$faults" && -d "$path" ]]
		then
			for f in $faults/fault*.php
			do
				read -r dst < $f
				dst=${dst/"#Destination: "}
				dst=${path}/${dst}
				echo "Injecting fault $f at $dst."
				cp $f $dst
			done
		else
			echo "Error: $faults and/or $path does not exist!"
		fi
	elif [ $1 == "reset" ]
	then
		if [[ -d "$path" ]]
		then
			for f in $faults/fault*.php
			do
				cd $path
				git reset
				git clean -f
				echo "Done."
			done
		else
			echo "Error: $path does not exist!"
		fi
	else
		echo "$usage"
	fi
else
	echo "$usage"
	if [ $# -ne 1 ]
	then
		echo "Warning: moodleMod requires 1 parameter and recieved $#."
	fi
	if [ "$0" != "./scripts/moodleMod.sh" ]
	then
		echo "Warning: moodleMod should be run from ../TestAutomation/."
	fi
fi
