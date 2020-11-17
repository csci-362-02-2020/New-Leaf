<?php

//
// htmlpurifier_UnitConverter.driver.php
//
// lukem1
// Newleaf
// 16 November 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "./project/moodle/lib/htmlpurifier/HTMLPurifier/UnitConverter.php";


// Input expression must be passed as a command line argument
if (!(sizeof($argv) == 2)) { 
	echo "Error: Expected args: [input] \n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($input) {
	//echo "Running Html2Text Test \n";
	//echo "Input: " . $input . "\n";
	
	$converter = new HTMLPurifier_UnitConverter();
	$output = $converter->getSigFigs($input);
	
	echo "{ \"output\": \"" . $output . "\" }";
}


// Run the test with command line input
$in = $argv[1];

test($in);

