<?php
	echo "start";
	$con = mysqli_connect("localhost","MM","mm","MM");
	
	echo "connected";
	//mysqli_query($con,"CREATE TABLE mouse_maps (mouse_id int,x_pos int,y_pos int,type_col int,option_col int)") or die(mysqli_error($con));
	echo "table created";
	
	for ($m=1;$m<=4;$m++)
	{
		for ($x=0;$x<=33;$x++)
		{
			for ($y=0;$y<=33;$y++)
			{	
				//echo $x.",".$y."<br>";
				mysqli_query($con,"INSERT INTO mouse_maps (mouse_id,x_pos,y_pos,type_col,option_col) VALUES (".$m.",".$x.",".$y.",0,0)") or die("ERROR");
			}
		}
	}
?>