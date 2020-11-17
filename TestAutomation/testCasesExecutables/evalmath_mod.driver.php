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
require "./project/moodle/lib/evalmath/evalmath.class.php";


// Input expression and expected output must be passed as command line arguments
// Warning: Input must not include spaces, if spaces are required this must be rewritten
if (!(sizeof($argv) == 2)) { 
	echo "Error: mod requires sizeof(\$argv) == 2 \n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($num, $modBy) {
	//echo "Running evalmath Test \n";
	//echo "Input: " . $num, $modBy . "\n";
	
	//echo $input;
	
	$math = new EvalMathFuncs;
	$output = $math->mod($num, $modBy);
	
	echo "{ \"output\": " . $output . " }";
}


// Run the test with command line input
$in = $argv[1];
//echo $in;
$ary = explode(",", $in );

test($ary[0], $ary[1]);

