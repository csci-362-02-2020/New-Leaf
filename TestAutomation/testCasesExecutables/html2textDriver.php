<?php

//
// html2textDriver.php
//
// lukem1
// Newleaf
// 4 November 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "./project/moodle/lib/html2text/Html2Text.php";


// Input expression and expected output must be passed as command line arguments
// Warning: Input must not include spaces, in this case the html must be encoded as base64
if (!(sizeof($argv) == 3)) { 
	echo "Error: html2textDriver requires sizeof(\$argv) == 3 \n";	
	return -1; 
}


// Method to perform a test
// Echos: {result, status}
function test($input, $expected) {
	//echo "Running Html2Text Test \n";
	//echo "Input: " . $input . "\n";
	//echo "Expected Output: " . $expected . "\n";
	
	$html = new Html2Text\Html2Text(base64_decode($input));
	$result = base64_encode($html->getText());
	//echo "Result: " . $result;
	//echo $input . " = " . $expected . " -> ";
	if ($result == $expected) {
		//echo "Test Passed.\n";
		$status = "Pass";
	}
	else {
		//cho "Test Failed.\n";
		$status = "Fail";
	}
	echo "{" . $result . ", " . $status . "}\n";
}


// Run the test with command line input
$in = $argv[1];
$expected = $argv[2];

test($in, $expected);

