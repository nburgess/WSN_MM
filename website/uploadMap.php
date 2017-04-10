<?php
	echo "v3";
	$con = mysqli_connect("localhost","MM","mm","MM");

	$MAP_SIZE=1089;//33 x 33

	$mouse=intval($_POST['mouse']);
	$options_raw=$_POST['options'];
	$types_raw=$_POST['types'];
	
	
	if ($mouse!=1 && $mouse!=2 && $mouse!=3 && $mouse!=4)
	{
		echo "INVALID MOUSE ID!";
		mysqli_query($con,"INSERT INTO log (msg) VALUES ('M_ID');") or die("ERROR");
		exit;
	}
	
	$options=json_decode($options_raw);
	$types=json_decode($types_raw);
	
	if (sizeof($options)!=$MAP_SIZE || sizeof($types)!=$MAP_SIZE)
	{
		echo "MAP WRONG SIZE";
		mysqli_query($con,"INSERT INTO log (msg) VALUES ('SIZE');") or die("ERROR");
		exit;
	}
	
	//echo $options[0].",";
	//echo $options[1].",";
	//echo $options[2].",";
	//echo $options[3].",";
	
	//echo $types[0].",";
	//echo $types[1].",";
	//echo $types[2].",";
	//echo $types[3].",";
	
	$count=0;
	for ($y=0;$y<=32;$y++)
	{
		for ($x=0;$x<=32;$x++)
		{	
			//echo $x.','.$y.'\n';
			mysqli_query($con,"UPDATE mouse_maps SET option_col=".intval($options[$count]).",type_col=".intval($types[$count])." WHERE mouse_id=".$mouse." AND x_pos=".$x." AND y_pos=".$y.";") or die("ERROR");
			$count++;
		}
	}

	mysqli_query($con,"INSERT INTO log (msg) VALUES ('SUCCESS');") or die("ERROR");
	echo "SUCCESS";
	
?>