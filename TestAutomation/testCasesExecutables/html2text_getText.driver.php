<?php

//
// html2text_getText.driver.php
//
// lukem1
// Newleaf
// 4 November 2020
//


// Requirements
require "./project/moodle/lib/html2text/Html2Text.php";


// Input must be passed as an argument
// Note: For this driver input/output is encoded in base64
if (!(sizeof($argv) == 2)) { 
	echo "Error: Driver expected 1 argument and recieved " . (sizeof($argv)-1) . ".\n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($input) {
	//echo "Input: " . $input . "\n";
	
	$html = new Html2Text\Html2Text(base64_decode($input));
	$output = base64_encode($html->getText());
	
	echo "{ \"output\": \"" . $output . "\" }";
}


// Run the test with input from argv

$in = $argv[1];

test($in);

