<?php
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
?>
<html>
	<head>
		<title> NitroXy <?=$event?> - NXGame </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
		<link rel="stylesheet" type="text/css" href="style.css"/>
	</head>
	<body>
		<div id="wrapper">
			<!-- Vi skall väl ha någon typ utav header? -->
			<div id="header">
				<h1> NXGame<?=$event?> </h1>
				<? if(is_loggedin()) { ?>
					<p> Inloggad som <?=$u->username?>, <a href="/user/logout"> logga ut </a></p>
				<? } else { ?>
					 <a href="/user/login"> Logga In </a> 
				<? } ?>
			</div>
			<!-- Navigation, antingen sidebar eller horisontell -->
			<div id="nav" class="nav">
				<ul>
					<li> <a href="/"> Startsida </a> </li>
					<li> <a href="/info"> Regler & Info </a> </li>
					<li> <a href="/game"> Game </a> </li>
			</div>
			<!-- ALl fucking content ! :D -->
			<div id="content">
				<?php
					try {
						$controller = Controller::factory($path);
						echo exec_controller($controller, $path);
					} catch(HTTPRedirect $e){
						header("Location: {$e->url}");
						exit();
					} catch (HTTPError $e){ 
						//TODO: add styling
						echo "<h2> {$e->title()} </h2> <p> {$e->message()} </p>";
					} catch(Exception $e){
						echo "<h2> Error </h2> <p> {$e->getMessage()} </p>";
					}
				?>
			</div>

			<!-- A footer ! -->
			<div id="footer">
				<p>Something about copyright here? </p>
			</div>
		</div>
	</body>
</html>
