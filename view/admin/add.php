<h2> Ny fråga </h2>
<?php
if($restore) { ?>
	<form action="/admin/add" method="post">
		Episod: <input type="text" name="episode" value="<?=$episode?>"/> <br><br>
		Nivå: <input type="text" name="level" value="<?=$level?>"/> <br><br>
		Fråga: <br>
		<textarea name="question" rows="4" cols="50"><?=$question?></textarea> <br><br>
		Svar: <input type="text" name="answer" value="<?=$answer?>"/> <br><br>
		<input type="submit" value="Spara"/>
	</form>
<? } else { ?>
	<form action="/admin/add" method="post">
		Episod: <input type="text" name="episode" value=""/> <br><br>
		Nivå: <input type="text" name="level" value=""/> <br><br>
		Fråga: <br>
		<textarea name="question" rows="4" cols="50"></textarea> <br><br>
		Svar: <input type="text" name="answer" value=""/> <br><br>
		<input type="submit" value="Spara"/>
	</form>
<? } ?>
