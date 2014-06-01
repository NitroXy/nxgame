<h2> Ändra fråga <?=$id?> </h2>
<p> Gamesyntax är en kombination utav både <a href="http://www.w3schools.com/html/default.asp">HTML</a> och <a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a>. Du kan välja helt själv i vad du vill skriva frågan i, till och med mixa :) </p>
<form action="/admin/edit/<?=$id?>" method="post">
 	<span>Episod: <input type="text" name="episode" value="<?=$episode?>"/> <br><br>
	Nivå: <input type="text" name="level" value="<?=$level?>"/> <br><br>
    Rubrik: <input type="text" name="title" value="<?=$title?>"/> <br><br>
	Fråga: <br>
	<textarea name="question" rows="20" cols="100"><?=$question?></textarea> <br><br>
    <input type="submit" name="updateQuestion" value="Uppdatera fråga">
</form>
<form action="/admin/edit/<?=$id?>" method="post">
    <br><br>
    <hr>
    <h2> Korrekta svar: </h2>
    <ul>
    <?php
    $a = NXGameAnswer::selection(array('ans_id' => $id));
    foreach($a as $i) {?>
        <li> <?=$i->answer?> 
            <a href="/admin/remove_answer/<?=$id?>/<?=$i->answer?>"><img src="/images/cross.png"></a></li>
    <?php }
    ?> 
    </ul>
	Lägg till svar: <input type="text" name="answer" value=""/> <br><br>
	<input type="submit" name="updateAnswers" value="Lägg till svar"/>
</form>
