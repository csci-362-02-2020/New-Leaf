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
# This script clones the moodle project (https://github.com/moodle/moodle) into /TestAutomation/project/moodle
#

usage="Usage: ./scripts/moodleMod.sh <action>
Actions:
  clone - clone the moodle project into project/moodle
  reset - delete project/moodle"
  
path="./project/moodle"

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
	elif [ $1 == "reset" ]
	then
		if [ -d "$path" ]
		then
			read -p "Confirm the deletion of $path (y/n)?" -n 1 -r
			if [[ $REPLY =~ ^[Yy]$ ]]
			then
				rm -rf $path
			fi
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
