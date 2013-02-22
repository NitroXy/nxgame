<?php

function is_loggedin() {
	global $u;
	return ($u != NULL);
}

function ensure_login() {
	global $u;
	if(is_loggedin()){
		throw new HTTPError403();
	}
}

function ensure_admin() {
	global $u;
	if(!$u && !$u->admin){
		throw new HTTPError403();
	}
}

function ensure_post() {
	//To be done
}

?>
