<?php

class AdminController extends Controller {
	public function pre_route($path) {
		ensure_login();
		ensure_admin();
	}

	public function index() { 
		global $event, $nxgame;
		return $this->render('index', array('event' => $event, 'nxgame' => $nxgame));
	}

	public function edit_game() {
		ensure_post();

		global $nxgame;
		$nxgame->current_episode = postdata('current_episode');
		$nxgame->final_episode = postdata('final_episode');
		$nxgame->winner = postdata('winner');
		$nxgame->commit();

		flash("success", "Ändringarna har sparats.");
		throw new HTTPRedirect("/admin");
	}

	public function create_next_game() {
		ensure_post();

		global $event;
		$game = new NXGame();
		$game->event = $event + 1;
		$game->current_episode = 1;
		$game->final_episode = 2;
		$game->commit();

		flash("success", "NXGame".($event + 1)." har skapats. Du behöver bara byta event i 'config.php' för att växla.");
		throw new HTTPRedirect("/admin");
	}

    public function remove_answer($id=null, $answer=null) {
        if($id == null || $answer == null) {
            flash("error", "DIN MAMMA GÖR FEL");
            throw new HTTPRedirect("/admin");
        }
        $q=NXGameQuestion::from_id($id);
		if(!$q) {
			flash("error", "Kunde inte hitta en fråga med id: {$id}");
			throw new HTTPRedirect("/admin");
		}
        $allAnswers = explode(",",$q->answer);
        foreach($allAnswers as $i => $answers) {
            if ($i == $answer) {
                unset($allAnswers[$i+1]);
            }
        }
        $q->answer = implode(",",$allAnswers);
        $q->commit();
        throw new HTTPRedirect("/admin/edit/$id");

                
    }

	public function edit($id=null) {
		if($id == null) {
			flash("error", "Kan inte redigera en fråga utan id");
			throw new HTTPRedirect("/admin");
		}

		$q = NXGameQuestion::from_id($id);
		if(!$q) {
			flash("error", "Kunde inte hitta en fråga med id: {$id}");
			throw new HTTPRedirect("/admin");
		}

		if(is_post()) {
            $allAnswers = explode(",",$q->answer);
            array_push($allAnswers, postdata('answer'));
			$q->episode = postdata('episode');
			$q->level = postdata('level');
			$q->question = postdata('question');
            $q->answer = implode(",",$allAnswers);
			$q->commit();

			flash("success", "Frågan har blivit ändrad.");
			throw new HTTPRedirect("/admin/edit/$id");
		}

		return $this->render("edit", array('id' => $id, 'question' => $q->question, 'episode' => $q->episode, 'level' => $q->level, 'answer' => $q->answer));
	}

	public function add() {
		if(is_post()) {
			global $event;
			
			//Check for empty fields
			if(postdata('episode') == "") {
				flash("error", "Episod är ett tomt fält.");
				return $this->render("add", array('restore' => 1, 'episode' => postdata('episode'), 'level' => postdata('level'), 'question' => postdata('question'), 'answer' => postdata('answer')));
			}
			if(postdata('level') == "") {
				flash("error", "Nivå är ett tomt fält.");
				return $this->render("add", array('restore' => 1, 'episode' => postdata('episode'), 'level' => postdata('level'), 'question' => postdata('question'), 'answer' => postdata('answer')));
			}
			if(postdata('question') == "") {
				flash("error", "En tom fråga?!?!?!?!");
				return $this->render("add", array('restore' => 1, 'episode' => postdata('episode'), 'level' => postdata('level'), 'question' => postdata('question'), 'answer' => postdata('answer')));
			}
			if(postdata('answer') == "") {
				flash("error", "En fråga utan svar, är du dum eller?");
				return $this->render("add", array('restore' => 1, 'episode' => postdata('episode'), 'level' => postdata('level'), 'question' => postdata('question'), 'answer' => postdata('answer')));
			}
			
			// Check if question already exists
			$t = NXGameQuestion::from_episode_and_level($event, postdata('episode'), postdata('level'));
			if($t) {
				flash("error", "Fråga ".postdata('level')." på episod ".postdata('episode')." finns redan.");
				return $this->render("add", array('restore' => 1, 'episode' => postdata('episode'), 'level' => postdata('level'), 'question' => postdata('question'), 'answer' => postdata('answer')));
			}

			$q = new NXGameQuestion();

			$q->event = $event;
			$q->episode = postdata('episode');
			$q->level = postdata('level');
			$q->question = postdata('question');
			$q->answer = postdata('answer');
			$q->commit();

			flash("success", "Frågan har skapats.");
			throw new HTTPRedirect("/admin");
		}

		return $this->render("add", array('restore' => 0));
	}

	public function get_answers($filter = null, $arg = null) {
		if($filter == null and $arg == null) {
			$answers = LogAnswer::selection(array("@order" => "id:desc"));
		} else if($filter == "name") {
			$answers = LogAnswer::selection(array("@order" => "id:desc", "user_id" => $arg));
		} else if($filter == "limit") {
			$answers = LogAnswer::selection(array("@order" => "id:desc", "@limit" => array(0, $arg)));
		}

		echo $this->render('get_answers', array('answers' => $answers));
		die();
	}
	public function answers() {
		return $this->render('answers');
	}
}

?>
