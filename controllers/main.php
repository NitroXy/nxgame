<?php

class MainController extends Controller {
	public function index() {
		global $u;
		if($u)
			$name = $u->username;
		else
			$name = "none";
		return $this->render('index', array('username' => $name));
	}
}
?>
