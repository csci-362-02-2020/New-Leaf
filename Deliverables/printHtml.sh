#! /usr/bin/bash

scripts= ls
echo $scripts
touch test.html
echo "<h1>$scripts</h1>" > test.html
xdg-open test.html
sleep 5
rm test.html
