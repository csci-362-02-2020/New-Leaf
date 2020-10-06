<?php

//
// exampleDriver.php
//
// lukem1
// Newleaf
// 30 September 2020
//

// TODO: Currently paths are relative, this script will only run from moodle/lib/classes

define('CLI_SCRIPT', true); // Tell moodle this is a cli script

require_once('../../config.php'); // Load moodle config from moodle/config.php

// User Creation, Access, Deletion Test

// Files
// moodle/user/lib.php
// moodle/lib/classes/user.php test

echo "loading moodle/user/lib.php \n";
require "../../user/lib.php";
echo "loading user.php \n";
require "./user.php";

// Create new user

// Fetch prexisting user to populate default values, then overwrite desired values

$core = new core_user;

$newuser = $core->get_user(2); // Fetch prexisting admin user with id 2

// The above simplifies manually creating an stdObject with the default attributes
// this would be done like this:
/*
$newuser = new stdClass();
$newuser->firstname = 'Tom';
$newuser->username = 'tomnook';
...
*/

// Overwrite uneeded or different values

$newuser->id = NULL;
$newuser->username = "tomnook";
$newuser->password = "NewLeaf-s3cr3t!";
$newuser->firstname = "Tom";
$newuser->lastname = "Nook";
$newuser->email = "tom@nookinc.biz";
$newuser->description = "Test user created by NewLeaf user generation script.";

$newuser_id = user_create_user($newuser); // Create new user

// Fetch new user from database

$fetched_user = $core->get_user($newuser_id);

print_r($fetched_user);

// Delete the new user

/*
This method leaves an entry in the database, which is somewhat messy, but it works.
Also, not a production server, so who cares.
*/

user_delete_user($fetched_user); // leaves user in db, marks as deleted


