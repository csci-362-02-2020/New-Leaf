<?php

//
// evalmath_mod.driver.php
//
// chris-m-taylor
// Newleaf
// 16 November 2020
//


// Requirements
require "./project/moodle/lib/evalmath/evalmath.class.php";


// Input must be passed as an argument
if (!(sizeof($argv) == 2)) { 
	echo "Error: Driver expected 1 argument and recieved " . (sizeof($argv)-1) . ".\n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($num, $modBy) {
	//echo "Input: " . $num, $modBy . "\n";
	
	$math = new EvalMathFuncs;
	$output = $math->mod($num, $modBy);
	
	echo "{ \"output\": " . $output . " }";
}


// Run the test with input from argv

$in = $argv[1];
$ary = explode(",", $in );

test($ary[0], $ary[1]);

