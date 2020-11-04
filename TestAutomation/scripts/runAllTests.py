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
import webbrowser

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
#print(testCases)

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


#format results
formattedResults = []

for result in results:
	formattedResults.append((result.stdout).decode("utf-8"))

print(formattedResults)
# Put results in html, open in web browser
htmlHead = """
<head>
<title>Current Directory</title>
  <style>
  
	body {   
		background-color: rgb(150, 108, 39);
	}
    
	h1 {
		display: flex;
		justify-content: center;
		color: rgb(255, 200, 53);
	}
    
	.scripts {
		display: flex;
		justify-content: center;
		color: rgb(243, 242, 236);
	}
    
	p {
		display: flex;
		text-align: left;
		justify-content: center;
	}
	
	h2 {
		display: flex;
		text-align: left;
		justify-content: center;
	}
    
    .button
	{
		border: none;
		border-radius: 12px;
		color: white;
		padding: 8px 16px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 12px;
	}
	.button:hover
	{
		box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
	}
	.wrapper
	{
		padding-bottom: 10px;
		text-align: center;
		justify-content: center;
	}
	
	.container
	{
		margin: 30px 5px;
		border: 2px solid black;
	}
    
  </style>
</head>
"""

htmlClosing = '''
</body> 
</html>'''

#create a temp file
tmpFile = "/tmp/newleaf-runAllTests.html"

with open(tmpFile, "w+") as file:
	file.write(htmlHead)
	
	#iterate through each test case
	for result in formattedResults:
		file.write("<div class='container'>")
		#split each result into array
		resultAry = result.split("\n")
		file.write("<h2>%s</h2>" % resultAry[0])
		file.write("<p>%s</p>" % resultAry[1])
		file.write("<p>%s</p>" % resultAry[2])
		file.write("<p>%s</p>" % resultAry[3])
		file.write("</div>")
	file.write(htmlClosing)
	
webbrowser.open(tmpFile)

















