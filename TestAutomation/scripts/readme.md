# scripts

This directory contains scripts used for running tests and other helper scripts.

## runAllTests.py

Runs all tests defined in ../testCases and displays the results in an html file.

Usage: `./scripts/runAllTests.py`

## moodleMod.sh

Automates common actions upon the moodle source code.

Usage: `./scripts/moodleMod.sh <action>`

Actions:

- clone
  - clone the moodle project into ./project/moodle
- delete
  - delete ../project/moodle
- inject
  - inject predefined faults from ../project/faults into moodle
- reset
  - clean and reset moodle to its original state

