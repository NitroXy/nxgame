<?php

function flash($class, $msg) {
	global $flash;
	if(!is_array($msg)) {
		$msg = array($msg);
	}

	if(!isset($flash[$class])) {
		$flash[$class] = array();
	} else if(!is_array($flash[$class])) {
		$flash[$class] = array($flash[$class]);
	}

	$flash[$class] = array_merge($flash[$class], $msg);
}

?>
