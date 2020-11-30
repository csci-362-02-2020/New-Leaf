<?php

//
// evalmath_ifthenelse.driver.php
//
// chris-m-taylor
// Newleaf
// 29 November 2020
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
function test($if, $then, $else) {
	//echo"Input: " . $if, $then, $else . "\n";
	
	$math = new EvalMathFuncs;
	$output = $math->ifthenelse($if, $then, $else);
	
	echo "{ \"output\": " . $output . " }";
}


// Run the test with command line input

$in = $argv[1];

$ary = explode(",", $in );

test($ary[0], $ary[1], $ary[2]);
