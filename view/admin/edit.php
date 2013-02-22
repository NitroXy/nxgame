<h2> Ändra fråga <?=$id?> </h2>
<form action="/admin/edit/<?=$id?>" method="post">
 	Episod: <input type="text" name="episode" value="<?=$episode?>"/> <br><br>
	Nivå: <input type="text" name="level" value="<?=$level?>"/> <br><br>
	Fråga: <br>
	<textarea name="question" rows="4" cols="50"><?=$question?></textarea> <br><br>
	Svar: <input type="text" name="answer" value="<?=$answer?>"/> <br><br>
	<input type="submit" value="Spara"/>
</form>
