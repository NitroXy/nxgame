<?php
	session_start();

	require("includes.php");

	//Get the path
	$path = Path::from_path_info();

	//Execute a controller
	function exec_controller($controller, $path) {
		//Run controller
		$controller->pre_route($path->args());
		$raw_content = $controller->route($path->args());

		return $raw_content;
	}

	//NXGame for this event
	$nxgame = NXGame::from_event($event);
	if(!$nxgame) {
		//wait wat?
		die("Error: could not find game entry for this event.");
	}

	$flash = array();
	if(isset($_SESSION['flash'])) {
		$flash = unserialize($_SESSION['flash']);
		unset($_SESSION['flash']);
	}

	//Build menu
	$menu = new Menu();
	$menu->AddItem("/", "Startsida", "main");
	$menu->AddItem("/info", "Regler & Info", "info");
	$menu->AddItem("/game", "Spela här", "game");
	if($u && $u->admin) {
		$menu->AddItem("/admin", "Admin", "admin");
	}

	//Display the controller
	try {
		$controller = Controller::factory($path);
		$content =  exec_controller($controller, $path);

	} catch(HTTPRedirect $e){
		//Set flash for next redirect
		if(isset($flash)) {
			$_SESSION['flash'] = serialize($flash);
		}

		header("Location: {$e->url}");
		exit();
	} catch (HTTPError $e){
		$error =  "<h2> {$e->title()} </h2> <p> {$e->message()} </p>";
	} catch(Exception $e){
		$error =  "<h2> Error </h2> <p> {$e->getMessage()} </p>";
	}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
	<head>
		<title> NitroXy <?=$event?> - NXGame </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
		<link rel="stylesheet" type="text/css" href="/style.css"/>
	</head>
	<body>
		<div id="wrapper">
			<div id="header">
				<h1> NXGame<?=$event?> </h1>
				<? if(is_loggedin()) { ?>
					<p> Inloggad som <?=$u->username?>, <a href="/user/logout"> logga ut </a></p>
				<? } else { ?>
					<p> <a href="/user/login"> Logga In </a> </p>
				<? } ?>
			</div>
			<div id="nav" class="nav">
				<?=$menu->render($path->controller());?>
			</div>
			<div id="content">
				<?php
					//Show flash messages
					foreach($flash as $class => $msg) {
						if(is_array($msg)) {
							foreach($msg as $m) {
								?> <p class="<?=$class?>"> <?=$m?> </p> <?
							}
						} else {
							?> <p class="<?=$class?>"> <?=$msg?> </p> <?
						}
					}

					//Show content
					if (isset($error)) {
						echo $error;
					}
					echo $content;
				?>
			</div>

			<div id="footer">
				<a href="images/derp.jpg"><p>Sidan är byggd utav cpluss, Renanyuu samt Ankan </p></a>
			</div>
		</div>
	</body>
</html>
