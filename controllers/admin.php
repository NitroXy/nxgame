<?php

class AdminController extends Controller {
	public function pre_route() {
		ensure_login();
		ensure_admin();
	}

	public function index() { 
		return $this->render('index');
	}
}

?>
