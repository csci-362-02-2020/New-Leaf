#!/usr/bin/env python3

#
# runAllTests.py
# scripts
#
# New-Leaf
# lukem1, chris-m-taylor, cafeheart
# 20 October 2020
#

testDir = "./testCases"
driverDir = "./testCasesExecutables"
outDir = "/tmp/newleaf-results.html"

from datetime import datetime
import json
import os
import subprocess
import webbrowser

# html used for building output file

headerSource = "./scripts/output_header.html"
footerSource = "./scripts/output_footer.html"

tableStart = """
<header><strong>NewLeaf Testing Framework Results</strong></header>
<p>%s</p> <!-- Date/time of execution -->

<table id="results">
  <tr>
  	<!-- Columns -->
    <th onclick="sortTable(0)">id</th>
    <th onclick="sortTable(1)">component</th>
    <th onclick="sortTable(2)">method</th>
    <th onclick="sortTable(3)">input</th>
    <th onclick="sortTable(4)">expected</th>
    <th onclick="sortTable(5)">output</th>
    <th onclick="sortTable(6)">result</th>
  </tr>
"""

tableRow = """
<tr>
    <td>%d</td> <!-- id -->
    <td>%s</td> <!-- component -->
    <td>%s</td> <!-- method -->
    <td>%s</td> <!-- input -->
    <td>%s</td> <!-- expected -->
    <td>%s</td> <!-- output -->
    <td class="%s">%s</td> <!-- class of result (pass/fail), text of result -->
</tr>
"""

# Required Test Case Fields
testCaseKeys = ['id', 'driver', 'requirement', 'component', 'method', 'input', 'expected']
outputKeys = ['id', 'component', 'method', 'input', 'expected', 'output', 'result']

# Malformed Test Case Exception
class MalformedTestError(Exception):
	def __init__(self, file, reason):
		self.file = file
		self.reason = reason


# Method to load a Test Case File
def loadTest(name):
	path = "%s/%s" % (testDir, name)
	case = None
	
	# Read Test Case file
	try:
		with open(path, "r") as file:
			case = json.load(file)
	except json.decoder.JSONDecodeError:
		raise MalformedTestError(name, "Bad json")
		
	# Check if all required keys exist
	missing = []
	for k in testCaseKeys:
		try:
			case[k]
		except KeyError:
			missing.append(k)
			
	if len(missing) > 0:
		raise MalformedTestError(name, "Missing keys %s" % missing)
		
	return case
	

# Method to Execute a Test Case File
def runTest(name):
	case = loadTest(name)
	
	# Execute the test
	driver =  "%s/%s" % (driverDir, case['driver'])
	testInput = str(case['input'])
	expected = str(case['expected'])
	
	if not os.path.exists(driver):
		raise MalformedTestError(name, "Driver not found (%s)" % driver)
		
	try:
		process = ["php", driver, testInput, expected]
		driverOut = subprocess.run(process, capture_output=True).stdout.decode("utf-8")
		driverOut = json.loads(driverOut)
	except:
		raise MalformedTestError(name, "Bad driver (%s)" % driver)
	
	# Add results to case and return
	
	case['output'] = driverOut['output']
	case['result'] = driverOut['result'] == 1 # true = pass, false = fail
	
	return case
	
	
# Run all Tests
def main():
	# Initialize output file
	
	out = open(outDir, "w+")
	
	with open(headerSource, "r") as header:
		for line in header:
			out.write(line)
			
	out.write(tableStart % datetime.now())
	
	# Begin processing and executing test cases 1 by one
	
	# Locate test case files
	testCases = []
	
	for t in os.scandir(testDir):
		name = t.name
		if len(name) > 5 and name[-5:] == ".json":
			testCases.append(name)
	
	skipped = 0
	for case in testCases:
		result = None
		try:
			result = runTest(case)
		except MalformedTestError as e:
			skipped += 1
			print("Skipping malformed test case: %s (%s)" % (e.reason, e.file))
			continue
			
		out.write("<tr>\n")
		for k in outputKeys:
			if k != "result":
				out.write("<td>"+str(result[k])+"</td>\n")
			else:
				s = "Fail"
				if result[k]:
					s = "Pass"
				out.write("<td class=\"%s\">%s</td>\n" % (s.lower(), s))
				
		out.write("</tr>\n")
		
	# Finalize output file and display results
	
	out.write("</table>\n")
	
	if skipped > 0:
		warning = "<p style=\"color: red\">Warning: %d test cases skipped due to errors, see stdout for more information.</p>\n" % skipped
		out.write(warning)
		
	with open(footerSource, "r") as footer:
		for line in footer:
			out.write(line)
			
	out.close()
	webbrowser.open(outDir)



if __name__ == "__main__":
	main()
