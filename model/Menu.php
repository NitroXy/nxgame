<?php

class MenuItem {
	private $href, $name, $ident;

	public function __construct($href, $name, $ident) {
		$this->href = $href;
		$this->name = $name;
		$this->ident = $ident;
	}

	public function render($sel) {
		if($sel == $this->ident) {
			$class = "selected";
		} else {
			$class = "";
		}
		echo'<li> <a class="'.$class.'" href="'.$this->href.'"> '.$this->name.' </a> </li>';
	}
}

class Menu {
	private $items = array();

	public function AddItem($href, $name, $ident) {
		array_push($this->items, new MenuItem($href, $name, $ident));
	}

	public function render($sel) {
		ob_start();

		echo "<ul>";
		foreach($this->items as $i) {
			$i->render($sel);
		}
		echo "</ul>";

		$content = ob_get_contents();
		ob_end_clean();

		return $content;
	}
}

?>
