<?php

function is_loggedin() {
	global $u;
	return ($u != NULL);
}

function ensure_login() {
	global $u;
	if(!is_loggedin()){
		throw new HTTPError403();
	}
}

function ensure_admin() {
	global $u;
	if(!$u && !$u->admin){
		throw new HTTPError403();
	}
}

/* no idea why I put it here ... */
function postdata($s) {
	return $_POST[$s];
}
function getdata($s) {
	return $_GET[$s];
}

function is_post() {
	return (strcasecmp($_SERVER['REQUEST_METHOD'], 'POST') == 0);
}

function ensure_post() {
	if(!is_post())
		throw new HTTPError403();
}

?>
