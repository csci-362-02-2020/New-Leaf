#! /bin/bash

ls > test.html
xdg-open test.html

sleep 5
rm test.html
