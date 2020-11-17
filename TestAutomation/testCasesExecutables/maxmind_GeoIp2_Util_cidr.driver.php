<?php

//
// maxmind_GeoIp2_Util_cidr.driver.php
//
// lukem1
// Newleaf
// 16 November 2020
//


// Requirements
// Note: Not part of moodle_internal, so no need to load moodle config
require "./project/moodle/lib/maxmind/GeoIp2/Util.php";


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
	$ary = explode("/", $input);
	
	$util = new GeoIp2\Util;
	$output = $util->cidr($ary[0], (int) $ary[1]);
	
	echo "{ \"output\": \"" . $output . "\" }";
}


// Run the test with command line input
$in = $argv[1];

test($in);

