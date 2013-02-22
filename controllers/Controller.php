<?php
/*
	Most of things from mvc_rewrite Controller class
*/

class HTTPRedirect extends Exception {
	public $url;

	public function __construct($url){
		parent::__construct();
		$this->url = $url;
	}
}

abstract class HTTPError extends Exception {
	public $code;
	public $data;

	public function __construct($code, $message=null, $data=null) {
		parent::__construct($message);
		$this->code = $code;
		$this->data = $data;
	}

	public abstract function set_http_status();
	public abstract function title();
	public abstract function message();
}

class HTTPError404 extends HTTPError {
	public function __construct() {
		parent::__construct(404);
	}

	public function set_http_status() {
		header('HTTP/1.1 404 Not Found');
	}

	public function title(){ return "404 Not Found"; }
	public function message(){ return "Sidan du försöker nå är inte tillgänglig."; }
}

class Controller {
	public $name;
	private $_PASSALONG = array();

	static public function factory($path) {
		if(!file_exists($path->filename())) {
			//Test if a view is present
			$controller = $path->controller();
			$view = $path->args();
			$view = count($view) > 0 ? $view[0] : 'index';

			$filename = "view/$controller/$view.php";
			if(file_exists($filename)) {
				return new SimpleController($path->controller());
			}

			throw new HTTPError404();
		}

		//Include the controller
		require($path->filename());
		//Create controller
		$classname = "{$path->controller()}Controller";
		return new $classname($path->controller());
	}

	public function __construct($name) {
		$this->name = $name;
	}

	/*
		Called before route, to do authentication
	*/
	public function pre_route($path) { }

	/*
		Check for a function named as the first index in $path, and if exists call it.
		Otherwise go for the 404.
	*/
	public function route($path) {
		$func = 'index';
		if(count($path) > 0) {
			$func = array_shift($path);
		}

		$func = array($this, $func);
		if(!is_callable($func)) {
			throw new HTTPError404();
		}

		return call_user_func_array($func, $path);
	}

	/*
		Render a view with filename $view
	*/
	public function render($view, $data=array()) {
		$path = $this->build_path_array($view);
		$this->_PASSALONG = $data;

		$filename = "view/" . implode("/", $path);
		return $this->_render_view($filename, $data, true);
	}

	public function _render_view($filename, $data=array(), $wrap) {
		$fullpath = "{$filename}.php";
		if(!file_exists($fullpath)){
			throw new HTTPError404();
		}

		extract($data);
		ob_start();
		require($fullpath);
		$content = ob_get_contents();
		ob_end_clean();

		return $content;
	}

	/* 
		Helper function to handle paths/urls
	*/
	private function build_path_array($arg) {
		if(is_array($arg)) {
			return $arg;
		} else {
			if(count($arg) > 0 && $arg[0] == "/") {
				$url = substr($arg, 1);
			} else {
				$url = "{$this->name}/$arg";
			}
			return explode("/", $url);
		}
	}
}

class SimpleController extends Controller {
	public function __call($name, $args) {
		BasicObject::$output_htmlspecialchars = true;
		return $this->render($name);
	}
}

?>
