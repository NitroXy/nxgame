<h2> Ändra fråga <?=$id?> </h2>
<p> Gamesyntax är en kombination utav både <a href="http://www.w3schools.com/html/default.asp">HTML</a> och <a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a>. Du kan välja helt själv i vad du vill skriva frågan i, till och med mixa :) </p>
<form action="/admin/edit/<?=$id?>" method="post">
 	<span>Episod: <input type="text" name="episode" value="<?=$episode?>"/> <br><br>
	Nivå: <input type="text" name="level" value="<?=$level?>"/> <br><br>
	Fråga: <br>
	<textarea name="question" rows="20" cols="120"><?=$question?></textarea> <br><br>
    Nuvarande svar: 
    <br> 
    <ul>
    <?php
    $allanswers = explode(',',$answer);
    foreach($allanswers as $i) {?>
        <li> <?=$i?> 
            <a href="/admin/remove_answer/<?=$id?>/<?=$i?>"><img src="/images/cross.png"></a></li>
    <?php }
    ?> 
    </ul>
	Lägg till svar (för flera svar, separera med komma): </span><input type="text" name="answer" value=""/> <br><br>
	<input type="submit" value="Spara"/>
</form>
