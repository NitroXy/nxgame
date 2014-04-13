<?php

class GameController extends Controller {
	public function index() {
		if(!is_loggedin()) {
			return '<p class="error"> Du måste vara inloggad för att delta i nxgame. </p>';
		}

		global $u, $event, $nxgame;

		//If not started nxgame yet, both episode and level hasn't been set
        if(!$nxgame->is_started) {
			return '<p>Nxgame har inte startat än.</p>';
        }

		if(!isset($u->episode) && !isset($u->level)) {
			$u->episode = 1;
			$u->level = 1;
			$u->commit();
		}

		//Finished nxgame?
		if(isset($u->finishtime)) {
			return '<p> Du har redan klarat av nxgame detta event. </p>';
		}
		
		// Get the question
		$q = NXGameQuestion::from_episode_and_level($event, $u->episode, $u->level);
		if($nxgame->current_episode < $u->episode) {
			return "<p class=\"info\"> Du har klarat av hela episod ".($u->episode - 1)." utav nxgame. Du måste vänta på att nästa episod skall börja för att fortsätta.</p>";
		} else if(!$q) {
			throw new Exception("What the hell? Contact admin.");
		}

		$question = NXGameQuestion::parse($q->question);
		return $this->render('index', array('question' => $question, 'episode' => $u->episode, 'level' => $u->level));
	}

	public function answer() {
		if(!is_loggedin()) {
			return '<p class="error"> Du måste vara inloggad för att delta i nxgame. </p>';
		}
		ensure_post();

		global $u, $event, $nxgame;

		$q = NXGameQuestion::from_episode_and_level($event, $u->episode, $u->level);
		$answer = strtolower(trim($_POST['answer']));
        $allAnswers = explode(",",$q->answer);
        foreach($allAnswers as $ans) {
            if ($answer == $ans) {
                $correct = True;
            }
        }

		AnswerLogger::Add($answer, ($answer == $q->answer));

		if(!$correct) {
			flash("error", "Du svarade fel.");
			throw new HTTPRedirect('/game');
		}

		//Progress to next level
		$q = NXGameQuestion::from_episode_and_level($event, $u->episode, $u->level + 1);
		if(!$q) {
			if($u->episode == $nxgame->final_episode) { // Finished nxgame?
				if(!isset($nxgame->winner)) {
					// User won nxgame
					$nxgame->winner = $u->username;
					$nxgame->commit();
				}

				// Update finished timestamp
				$u->finishtime = date('Y:m:d H-i-s');	
				$u->commit();

				if($nxgame->winner == $u->username) {
					throw new HTTPRedirect('/game/won');
				} else {
					throw new HTTPRedirect('/game/finish');
				}
			} else {
				$u->episode = $u->episode + 1;
				$u->level = 1;
				$u->commit();

				flash("success", "Du har klarat av hela episod ".($u->episode - 1));
				throw new HTTPRedirect('/game');
			}
		}
		
		//Next level
		$u->level = $u->level + 1;
		$u->commit();


		flash("success", "Du svarade rätt.");
		throw new HTTPRedirect('/game');
	}

	public function won() {
		return $this->render('won');
	}

	public function finish() {
		return $this->render('finish');
	}
}

?>
