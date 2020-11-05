<?php

//
// evalmathDriver.php
//
// lukem1
// Newleaf
// 19 October 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "../project/moodle/lib/evalmath/evalmath.class.php";


// Input expression and expected output must be passed as command line arguments
// Warning: Input must not include spaces, if spaces are required this must be rewritten
if (!(sizeof($argv) == 3)) { 
	echo "Error: evalmathDriver requires sizeof(\$argv) == 3 \n";	
	return -1; 
}


// Method to perform a test
// Echos: {module, input, expected, result, status}
function test($input, $expected) {
	//echo "Running evalmath Test \n";
	//echo "Input: " . $input . "\n";
	//echo "Expected Output: " . $expected . "\n";
	
	$math = new EvalMath;
	$result = $math->evaluate($input);
	
	//echo $input . " = " . $expected . " -> ";
	if ($result == $expected) {
		//echo "Test Passed.\n";
		$status = "Pass";
	}
	else {
		//echo "Test Failed.\n";
		$status = "Fail";
	}
	echo "{" . "evalmath" . ", " . $input . ", " . $expected . ", " . $result . ", " . $status . "}\n";
}


// Run the test with command line input
$in = $argv[1];
$expected = (int) $argv[2];

test($in, $expected);

