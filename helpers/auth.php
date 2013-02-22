<?php

require_once("nxauth.php");

phpCAS::setNoCasServerValidation();

if(phpCAS::isAuthenticated()) {
	$attr = phpCAS::getAttributes();
	$u = User::find_or_create_from_cas();
} else {
	$u = NULL;
}

?>
