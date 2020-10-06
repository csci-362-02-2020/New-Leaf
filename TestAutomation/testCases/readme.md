# testCases

## Defining Test Cases

Test cases should be json files with the name testCasex.json where x is the test case number.

Thes files shoud be in the following format:

{ 
	“id”: x,
	“requirement”: “Requirement”,
	“component”: “Component Name”,
	“method”: “Method Name”,
	“input”: “input”,
	“output”: “output”
}

where the fields are defined as follows:
1. test number or ID
2. requirement being tested
3. component being tested
4. method being tested
5. test input(s) including command-line argument(s)
6. expected outcome(s)

