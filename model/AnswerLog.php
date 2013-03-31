<?php

class LogAnswer extends BasicObject {
	protected static function table_name() {
		return 'answers';
	}
}

class AnswerLogger {
	public static function Add($answer, $correct) {
		global $u;

		$ans = new LogAnswer;
		$ans->user_id = $u->user_id;
		$ans->episode = $u->episode;
		$ans->level = $u->level;
		$ans->answer = $answer;
		$ans->correct = $correct;

		$ans->commit();
	}
}

?>
