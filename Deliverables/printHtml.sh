#! /usr/bin/bash

read scripts <<< "$(ls)"
echo $scripts
echo "<h1>$scripts</h1>" > test.html
xdg-open test.html
sleep 5
rm test.html
