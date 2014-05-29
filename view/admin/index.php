<h2> Admin </h2>
<p> Nuvarande event: <?=$event?> </p>

<div class="info">
	<h3> Game: </h3>
<form method="post" action="/admin/edit_game">
	<span>Nuvarande episod:</span> <input type="text" name="current_episode" value="<?=$nxgame->current_episode?>"/> </br>
	<span>Sista episod: </span><input type="text" name="final_episode" value="<?=$nxgame->final_episode?>"/> </br>
	<span>Vinnare: </span><input type="text" name="winner" value="<?=$nxgame->winner?>"/> </br>
	<span>Är igång </span><input type="checkbox" name="is_started" value="1"
    <?php
    if ($nxgame->is_started) {
        echo "checked";
    } ?>>
</br></br>
	<input type="submit" name="submit" value="Spara"/>
</form>

<form method="post" action="/admin/create_next_game">
	<input type="submit" name="submit" value="Skapa nästa Game (NXGame<?=($event + 1)?>)"/>
</form>
</div>

<div class="info">
	<p> För att se alla svaren, klicka <a href="/admin/answers">här</a> </p>
</div>

<div class="info">
	<h3> Frågor </h3>

	<?php
		$episode = 1;
		while($episode <= $nxgame->final_episode) {
			?> <h4> Episod <?=$episode?> </h4> <?
			foreach($nxgame->questions($episode) as $q) {
				?> 
					<span>Fråga <?=$q->level?> - <?=$q->title?> - <a href="/admin/edit/<?=$q->id?>"> Ändra </a></span>
					</br>
				<?	
			}

			$episode = $episode + 1;
		}
	?>

	<p> <a href="/admin/add"> Skapa ny fråga </a> </p>

</div>
