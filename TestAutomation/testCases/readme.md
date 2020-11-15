# testCases

## Defining Test Cases

Test cases should be json files with the name testCasex.json where x is the test case number.

Thes files shoud be in the following format:

{ 
	“id”: x,
	"driver": "testCasex.php",
	“requirement”: “Requirement”,
	“component”: “Component Name”,
	“method”: “Method Name”,
	“input”: “input”,
	“expected”: “expected output”
}

where the fields are defined as follows:
1. test number or ID
2. filename of driver found in testCaseExecutables
3. requirement being tested
4. component being tested
5. method being tested
6. test input(s) including command-line argument(s)
7. expected outcome(s)

## Malformed Test Cases

This directory contains a couple files named malformedx.json, these are malformed testcases that show that the framework is able to handle bad test cases.
