<?php

class User extends BasicObject {
	protected static function table_name(){
		return 'user';
	}

	public static function find_or_create_from_cas() {
		$attr = phpCAS::getAttributes();
		$user = static::selection(array("user_id" => $attr["user_id"]));
		if(!$user) {
			$user = new User();
			$user->user_id = $attr["user_id"];
			$user->username = phpCAS::getUser();
			$user->name = $attr["fullname"];
			$user->admin = false;
			$user->commit();
		} else {
			$user = $user[0];
		}
		
		return $user;
	}
}
	
?>
