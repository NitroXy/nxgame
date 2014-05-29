<h1> Episod <?=$episode?> - Nivå <?=$level?> </h1>
<h2> <? echo $title; ?></h2>
<p> <? echo $question; ?> </p>

<form method="post" action="/game/answer">
	Svar: <input type="text" name="answer" value=""/>
	<input type="submit" name="Svara" value="Svara"/>
</form>
