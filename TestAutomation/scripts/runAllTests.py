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

testsDir = "../testCases"
exesDir = "../testCasesExecutables"

import json
import os

# Read testCases, exes Dirs

testCaseDefs = []
exes = []

# Find all .json file names in testsDir
for t in os.scandir(testsDir):
	name = t.name
	try:
		split = name.split('.')
		if len(split) == 2 and split[1] == "json":
			testCaseDefs.append(name)
	except:
		pass
			
print("Found testCases:")
print(testCaseDefs)

# Find all .php file namess in exesDir
for e in os.scandir(exesDir):
	name = e.name
	try:
		split = name.split('.')
		if len(split) == 2 and split[1] == "php":
			exes.append(name)
	except:
		pass

print("Found Drivers:")
print(exes)

# Load testcases

testCases = []

for t in testCaseDefs:
	path = "%s/%s" % (testsDir, t)
	with open(path, "r") as file:
		testCases.append(json.load(file))
		
# Sort testCases by id number
testCases = sorted(testCases, key=lambda k: k['id']) 

print("Loaded Test Cases:")
print(testCases)

# Run testCases, parse and compile results

# Put results in html, open in web browser









