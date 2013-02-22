<?php
require_once "libs/php-markdown/Michelf/Markdown.php";
require_once "libs/php-markdown/Michelf/MarkdownExtra.php";
use \Michelf\MarkdownExtra;

class NXGameQuestion extends BasicObject {
	protected static function table_name() {
		return 'questions';
	}

	public static function from_episode_and_level($event, $episode, $level) {
		$sel = static::selection(array('event' => $event, 'episode' => $episode, 'level' => $level));
		if(empty($sel)) {
			return null;
		}

		return $sel[0];
	}
	public static function from_episode($event, $episode) {
		return static::selection(array('event' => $event, 'episode' => $episode));
	}

	public static function parse($text) {
		$markdown = new MarkdownExtra();

		$markdown->no_markup = true;
		$markdown->nl2br = true;

		return html_entity_decode($markdown->transform($text), ENT_QUOTES, "UTF-8");
	}

	public function question(){ return $question; }
	public function answer() { return $answer; }
	public function episode() { return $episode; }
	public function level() { return $level; }
}

class NXGame extends BasicObject {
	protected static function table_name() {
		return 'game';
	}

	static function from_event($ev) {
		return static::from_field('event', $ev);
	}

	public function questions($episode) {
		return NXGameQuestion::from_episode($this->event, $episode);
	}
}

?>
