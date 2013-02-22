<h2> Episod <?=$episode?> - Nivå <?=$level?> </h2>
<p> <?=$question?> </p>

<form method="post" action="/game/answer">
	Svar: <input type="text" name="answer" value=""/>
	<input type="submit" name="Svara" value="Svara"/>
</form>
