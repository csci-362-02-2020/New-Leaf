#!/usr/bin/env python3

#
# runAllTests.py
# scripts
#
# New-Leaf
# lukem1, chris-m-taylor, cafeheart
# 20 October 2020
#

# TODO: Script and drivers are currently designed to run with the TestAutomation dir in the moodle project's root directory

testDir = "../testCases"
driverDir = "../testCasesExecutables"

import json
import os

# Read testDir, driverDir

testCaseDefs = []
drivers = []

# Find all .json file names in testDir
for t in os.scandir(testDir):
	name = t.name
	try:
		split = name.split('.')
		if len(split) == 2 and split[1] == "json":
			testCaseDefs.append(name)
	except:
		pass
			
print("Found testCases:")
print(testCaseDefs)

# Find all .php file names in driverDir
for e in os.scandir(driverDir):
	name = e.name
	try:
		split = name.split('.')
		if len(split) == 2 and split[1] == "php":
			drivers.append(name)
	except:
		pass

print("Found Drivers:")
print(drivers)

# Load testcases

testCases = []

for t in testCaseDefs:
	path = "%s/%s" % (testDir, t)
	with open(path, "r") as file:
		testCases.append(json.load(file))
		
# Sort testCases by id number
testCases = sorted(testCases, key=lambda k: k['id']) 

print("Loaded Test Cases:")
print(testCases)

# Run testCases, parse and compile results

# Put results in html, open in web browser









