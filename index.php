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
?>
<html>
	<head>
		<title> NitroXy <?=$event?> - NXGame </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
		<link rel="stylesheet" type="text/css" href="/style.css"/>
	</head>
	<body>
		<div id="wrapper">
			<!-- Vi skall väl ha någon typ utav header? -->
			<div id="header">
				<h1> NXGame<?=$event?> </h1>
				<? if(is_loggedin()) { ?>
					<p> Inloggad som <?=$u->username?>, <a href="/user/logout"> logga ut </a></p>
				<? } else { ?>
					<p> <a href="/user/login"> Logga In </a> </p>
				<? } ?>
			</div>
			<!-- Navigation, antingen sidebar eller horisontell -->
			<div id="nav" class="nav">
				<ul>
					<li> <a href="/"> Startsida </a> </li>
					<li> <a href="/info"> Regler & Info </a> </li>
					<li> <a href="/game"> Game </a> </li>
					<? if($u && $u->admin) { ?>
						<li> <a href="/admin"> Admin </a> </li>
					<? } ?>
				</ul>
			</div>
			<!-- ALl fucking content ! :D -->
			<div id="content">
				<?php

					//Display the controller
					try {
						$controller = Controller::factory($path);
						$content =  exec_controller($controller, $path);

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
						echo $content;
					} catch(HTTPRedirect $e){
						//Set flash for next redirect
						if(isset($flash)) {
							$_SESSION['flash'] = serialize($flash);
						}

						header("Location: {$e->url}");
						exit();
					} catch (HTTPError $e){ 
						echo "<h2> {$e->title()} </h2> <p> {$e->message()} </p>";
					} catch(Exception $e){
						echo "<h2> Error </h2> <p> {$e->getMessage()} </p>";
					}
				?>
			</div>

			<!-- A footer ! -->
			<div id="footer">
				<p>Sidan är byggd utav cpluss, Renanyuu samt Ankan </p>
			</div>
		</div>
	</body>
</html>
