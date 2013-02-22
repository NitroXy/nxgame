<?php

class NXGameQuestion extends BasicObject {
	protected $text;
	protected $answer;

	public function text(){ return $text; }
	public function answer() { return $answer; }
}

class NXGame extends BasicObject {
	private $stage;
}

?>
