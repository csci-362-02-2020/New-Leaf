# testCasesExecutables

This directory contains the drivers which are responsible for interacting with the moodle source code and providing an interface for the runAllTests script to execute test cases on a class or method.

# Creating Drivers

Each driver must accept input to pass to the method being tested within moodle as an argument and return the output to stdout as a json string in the format "{ "output": output }".
