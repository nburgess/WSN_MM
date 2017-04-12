<?php
	echo "v4";
	$con = mysqli_connect("localhost","MM","mm","MM");

	$line=$_POST['line'];
	mysqli_query($con,"INSERT INTO network_data (line) VALUES ('".mysql_escape_string($line)."');") or die("ERROR");
	
	echo "SUCCESS";
?>