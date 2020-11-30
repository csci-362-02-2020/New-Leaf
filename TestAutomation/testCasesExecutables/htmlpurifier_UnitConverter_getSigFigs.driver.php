<?php

//
// htmlpurifier_UnitConverter_getSigFigs.driver.php
//
// lukem1
// Newleaf
// 16 November 2020
//


// Requirements
require "./project/moodle/lib/htmlpurifier/HTMLPurifier/UnitConverter.php";


// Input must be passed as an argument
if (!(sizeof($argv) == 2)) { 
	echo "Error: Driver expected 1 argument and recieved " . (sizeof($argv)-1) . ".\n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($input) {
	//echo "Input: " . $input . "\n";
	
	$converter = new HTMLPurifier_UnitConverter();
	$output = $converter->getSigFigs($input);
	
	echo "{ \"output\": \"" . $output . "\" }";
}


// Run the test with input from argv

$in = $argv[1];

test($in);

