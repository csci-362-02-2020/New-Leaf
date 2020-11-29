# New-Leaf's Team Repo

## Quickstart

1. Clone this repository and change directory into the created repository and then TestAutomation

`git clone https://github.com/csci-362-02-2020/New-Leaf`

`cd New-Leaf`

`cd TestAutomation`

2. Use the moodleMod script to clone the moodle project into ./TestAutomation/project/moodle/

`./scripts/moodleMod.sh clone`

3. (Optional) Inject faults into the moodle source code

`./scripts/moodleMod.sh inject`

To revert these changes run: `./scripts/moodleMod.sh reset`

4. Run the tests! It is expected to see errors due to the three intentionally wrong test cases.

`./scripts/runAllTests.py`

## Navigating this Project

Check out this project's wiki to find detailed information about various aspects of this project including the timeline, details on how to write test cases/drivers, and documentation which can also be found in the readme.md files scattered throughout this project.

Additionally, the Deliverables directory contains all of our teams reports and presentations.

## The Team
- [Luke McGuire](https://github.com/lukem1)
- [Chris Taylor](https://github.com/chris-m-taylor)
- [Kasper Dugaw](https://github.com/cafeheart)
