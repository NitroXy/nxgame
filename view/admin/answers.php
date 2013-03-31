<script type="text/javascript">
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

		xmlhttp.open("GET", "/admin/get_answers", true);
		xmlhttp.send();
	}

	setInterval(onupdate, 3000);
	onupdate();
</script>

<div id="answers">
	<p> Uppdateras ... </p>
</div>
