<div id="answers">
<p>
<table>
	<tr> <th> Timestamp </th> <th> Episod </th> <th> Nivå </th> <th> Namn </th> <th> Svar: </th> </tr>
<?php
	foreach($answers as $ans) { ?>
		<tr>
			<td style="padding-right: 30px"> <?=$ans->timestamp?> </td>
			<td> <?=$ans->episode?> </td>
			<td style="padding-right:30px"> <?=$ans->level?> </td>
			<td style="padding-right:30px"> <?=$ans->User->name?> </td>
			<td style="padding-right:50px"> <?=$ans->answer?> </td>
			<td> <?=(($ans->correct == 1) ? "<span class=\"correct\">rätt</span>" : "<span class=\"wrong\">fel</span>")?> </td>
		</tr>
<?	}
?>
</table>
</p>
</div>
