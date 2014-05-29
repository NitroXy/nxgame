<h2> Ny fråga </h2>
<p> Gamesyntax är en kombination utav både <a href="http://www.w3schools.com/html/default.asp">HTML</a> och <a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a>. Du kan välja helt själv i vad du vill skriva frågan i, till och med mixa :) </p>
<?php
if($restore) { ?>
	<form action="/admin/add" method="post">
		Episod: <input type="text" name="episode" value="<?=$episode?>"/> <br><br>
		Nivå: <input type="text" name="level" value="<?=$level?>"/> <br><br>
        Rubrik: <input type="text" name="title" value="<?=$title?>"/> <br><br>
		Fråga: <br>
		<textarea name="question" rows="4" cols="50"><?=$question?></textarea> <br><br>
		Svar: <input type="text" name="answer" value="<?=$answer?>"/> <br><br>
		<input type="submit" value="Spara"/>
	</form>
<? } else { ?>
	<form action="/admin/add" method="post">
		Episod: <input type="text" name="episode" value=""/> <br><br>
		Nivå: <input type="text" name="level" value=""/> <br><br>
        Rubrik: <input type="text" name="title" value=""> <br><br>
		Fråga: <br>
		<textarea name="question" rows="4" cols="50"></textarea> <br><br>
		Svar: <input type="text" name="answer" value=""/> <br><br>
		<input type="submit" value="Spara"/>
	</form>
<? } ?>
