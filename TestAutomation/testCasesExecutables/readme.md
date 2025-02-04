# testCasesExecutables

This directory contains the drivers which are responsible for interacting with the moodle source code and providing an interface for the runAllTests script to execute test cases on a class or method.

# Creating Drivers

Drivers are pretty flexible, but there are three key details to keep in mind when creating a driver:

1. Each driver must accept input to pass to the method being tested within moodle as an argument.

2. Each driver must return the output generated by the moodle source code to stdout as a json string in the format `{ "output": output }`.

3. Be aware of the [test case specifications](https://github.com/csci-362-02-2020/New-Leaf/blob/master/TestAutomation/testCases/readme.md).
