<?php

//
// evalmath_.php
//
// lukem1, chris-m-taylor
// Newleaf
// 19 October 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "./project/moodle/lib/evalmath/evalmath.class.php";


// Input expression and expected output must be passed as command line arguments
// Warning: Input must not include spaces, if spaces are required this must be rewritten
if (!(sizeof($argv) == 2)) { 
	echo "Error: mod requires sizeof(\$argv) == 2 \n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($if, $then, $else) {
	//echo "Running evalmath Test \n";
	//echo"Input: " . $if, $then, $else . "\n";
	
	//echo $input;
	
	$math = new EvalMathFuncs;
	$output = $math->ifthenelse($if, $then, $else);
	
	echo "{ \"output\": " . $output . " }";
}


// Run the test with command line input
$in = $argv[1];
//echo $in;
$ary = explode(",", $in );

test($ary[0], $ary[1], $ary[2]);
