<?php

//
// maxmind_GeoIp2_Util_cidr.driver.php
//
// lukem1
// Newleaf
// 16 November 2020
//


// Requirements\
require "./project/moodle/lib/maxmind/GeoIp2/Util.php";


// Input must be passed as arguments
if (!(sizeof($argv) == 2)) { 
	echo "Error: Driver expected 1 argument and recieved " . (sizeof($argv)-1) . ".\n";	
	return -1; 
}


// Method to perform a test
// Echos: { "output": output }
function test($input) {
	//echo "Input: " . $input . "\n";
	
	$ary = explode("/", $input);
	
	$util = new GeoIp2\Util;
	$output = $util->cidr($ary[0], (int) $ary[1]);
	
	echo "{ \"output\": \"" . $output . "\" }";
}


// Run the test with input from argv

$in = $argv[1];

test($in);

