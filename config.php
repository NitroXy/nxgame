<?php

class Config {
	private static $db_host = "localhost";
	private static $db_name = "nxgame";
	private static $db_user = "nxgame";
	private static $db_password = "nxgamelol";

	public static function fix_database($username=null) {
		if(is_null($username)) {
			$username = self::$db_user;
			$password = self::$db_password;
		}
		return new MySQLi(self::$db_host, $username, $password, self::$db_name);
	}
}

require_once("model/BasicObject.php");
require_once("model/ValidatingBasicObject.php");
BasicObject::$output_htmlspecialchars = true;

$db = Config::fix_database();
$event = 21;
$dir = dirname(__FILE__);
?>
