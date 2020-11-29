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


// Input must be passed as arguments
// Warning: Input must not include spaces, in this case the html must be encoded as base64
if (!(sizeof($argv) == 2)) { 
	echo "Error: html2textDriver requires sizeof(\$argv) == 2 \n";	
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

