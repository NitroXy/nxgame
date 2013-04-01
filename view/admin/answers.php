<script type="text/javascript">
	var link = "/admin/get_answers/limit/30";

	function onupdate() {
		var xmlhttp, parser;
		if(window.XMLHttpRequest) {
			xmlhttp = new XMLHttpRequest();
		} else {
			xmlhttp = ActiveXObject("Microsoft.XMLHTTP");
		}

		xmlhttp.onreadystatechange = function() {
				if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
					document.getElementById("answers").innerHTML = xmlhttp.responseText;
				}
			}

		xmlhttp.open("GET", link, true);
		xmlhttp.send();
	}

	function limitchange() {
		link = "/admin/get_answers/limit/" + document.getElementById("limit").value;
		onupdate();
	}

	setInterval(onupdate, 3000);
	onupdate();
</script>

<div class="info">
	<p> Visa <input type="text" name="limit" id="limit" value="30" onchange="limitchange()"/> element. </p>
</div>

<div class="info">
	<div id="answers">
		<p> Uppdateras ... </p>
	</div>
</div>
