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
import subprocess

# Read testDir

testCaseDefs = []

# Find all .json file names in testDir
for t in os.scandir(testDir):
	name = t.name
	try:
		split = name.split('.')
		if len(split) == 2 and split[1] == "json":
			testCaseDefs.append(name)
	except:
		pass

# Load testcases

testCases = []

for t in testCaseDefs:
	path = "%s/%s" % (testDir, t)
	with open(path, "r") as file: #using with to avoid closing the file
		testCases.append(json.load(file)) #json.load(file) turns the file into a dictonary
		
# Sort testCases by id number testcases[0]['requirement'] => value of requirement
testCases = sorted(testCases, key=lambda k: k['id']) 

print("Loaded Test Cases:")
print(testCases)

# Run testCases, parse and compile results

results = []
for case in testCases:

	nameOfDriver =  "%s/%s" % (driverDir, case['driver'])
	testInput = str(case['input'])
	expectedOutput = str(case['output'])
	process = ["php", nameOfDriver, testInput, expectedOutput]

	#capture the output
	capturedOutput = subprocess.run(process, capture_output=True)
	
	#append to array
	results.append(capturedOutput)

print(results)


#format results


# Put results in html, open in web browser









