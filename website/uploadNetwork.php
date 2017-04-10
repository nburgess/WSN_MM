<?php
	echo "v1";
	$con = mysqli_connect("localhost","MM","mm","MM");

	$lines_raw=intval($_POST['lines']);
	
	$lines=json_decode($lines_raw);
	
	$count=0;
	for ($n=0;$n<sizeof($lines);$n++)
	{
		mysqli_query($con,"INSERT INTO network_data (line) VALUES ('".$lines[$n]."');") or die("ERROR");
	}

	mysqli_query($con,"INSERT INTO log (msg) VALUES ('S2');") or die("ERROR2");
	echo "SUCCESS";
	
?>