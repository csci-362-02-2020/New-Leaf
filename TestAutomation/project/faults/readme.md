# faults

This directory contains predefined faults that can be injected into moodle using the moodleMod script.

## Defining Faults

Faults should be named with this pattern, where * is an integer: fault*.php

The first line of any fault file should contain the destination of the file formatted as follows:

`<?php #Destination: ./dst`

Where dst is the path of the file from ../moodle/.

## Injecting Faults

Running the moodleMod script as follows will copy the faults in this directory to their specified destinations:

`./scripts/moodleMod.sh inject`

The moodleMod script can also be used to remove the faults and reset moodle by using the reset option:

`./scripts/moodleMod.sh reset`

As with all other scripts, the moodleMod method should be executed from ../TestAutomation/.

## Predefined Faults

### fault1.php

../moodle/lib/html2text/Html2Text.php

Line 144 changed so that the class improperly handles html with \<br\> elements.

`'/<(br)[^>]*>[ ]*/i',` to `'/<(brk)[^>]*>[ ]*/i',`

This fault causes the test case with the following id to fail: 8

### fault2.php

./moodle/lib/maxmind/GeoIp2/Util.php

Line 23 changed so that the loop executes 1 time less then necessary.

`for ($i = 0; $i < \strlen($ipBytes) && $curPrefix > 0; $i++) {`

to

`for ($i = 0; $i < \strlen($ipBytes)-1 && $curPrefix > 0; $i++) {`

This fault causes the test case with the following id to fail: 12

### fault3.php

./moodle/lib/htmlpurifier/HTMLPurifier/UnitConverter.php

Line 194 changed so that negative numbers are improperly handled.

`$n = ltrim($n, '0+-');` to `$n = ltrim($n, '0+');`

This fault causes the test case with the following id to fail: 19

### fault4-5.php

./moodle/lib/evalmath/evalmath.class.php

#### 4

Line 436 changed so that expressions with subtraction throw an error.

`} elseif (in_array($token, array('+', '-', '*', '/', '^', '>', '<', '==', '<=', '>='), true)) {`

to

`} elseif (in_array($token, array('+', '+', '*', '/', '^', '>', '<', '==', '<=', '>='), true)) {`

This fault causes the test case with the following id to fail: 2

#### 5

Line 586 changed so that mod is calculated incorrectly.

'return $op1 % $op2;' to `return $op2 % $op1;`

This fault causes the test cases with the following ids to fail: 22, 23, 24



