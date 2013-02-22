<?php

class UserController extends Controller {
	public function login() {
		phpCAS::forceAuthentication();
		throw new HTTPRedirect("/");
	}

	public function logout() {
		phpCAS::logout();
		throw new HTTPRedirect("/");
	}
}

?>
