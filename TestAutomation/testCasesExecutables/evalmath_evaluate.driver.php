<?php

//
// evalmath_evaluate.driver.php
//
// lukem1, chris-m-taylor
// Newleaf
// 19 October 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "./project/moodle/lib/evalmath/evalmath.class.php";


// Input must be passed as an argument
if (!(sizeof($argv) == 2)) { 
	echo "Error: Driver expected 1 argument and recieved " . (sizeof($argv)-1) . ".\n";		
	return -1; 
}


// Method to perform a test
// Echos: { "output": output}
function test($input) {
	//echo "Input: " . $input . "\n";
	
	$math = new EvalMath;
	$output = $math->evaluate($input);
	
	echo "{ \"output\": " . $output . " }";
}


// Run the test with command line input

$in = $argv[1];

test($in);

