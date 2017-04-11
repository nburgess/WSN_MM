<?php
	$con = mysqli_connect("localhost","MM","mm","MM");
	
	$map_datas4=mysqli_query($con,"SELECT line FROM network_data") or die("ERROR");

	
	$map_datas1=mysqli_query($con,"SELECT option_col,type_col,x_pos,y_pos FROM mouse_maps WHERE mouse_id=1 ORDER BY y_pos ASC,x_pos ASC") or die("ERROR");
	$map_datas2=mysqli_query($con,"SELECT option_col,type_col,x_pos,y_pos FROM mouse_maps WHERE mouse_id=2 ORDER BY y_pos ASC,x_pos ASC") or die("ERROR");
	$map_datas3=mysqli_query($con,"SELECT option_col,type_col,x_pos,y_pos FROM mouse_maps WHERE mouse_id=3 ORDER BY y_pos ASC,x_pos ASC") or die("ERROR");
	$map_datas4=mysqli_query($con,"SELECT option_col,type_col,x_pos,y_pos FROM mouse_maps WHERE mouse_id=4 ORDER BY y_pos ASC,x_pos ASC") or die("ERROR");
?>

<html>
    <head>
        <title>Virtual Micromouse Project</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body style="background-color:#FFACD;font: normal 100% 'century gothic', arial, sans-serif;">


        <div>
          <div id="banner">
            <div id="banner-content" align="center">
              <img src="logo2.png" alt="Mountain View" style="width:600px;height:69px;">
            </div>
          </div>
          <ul id="nav" align="center">
                    <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
                    <li class="selected"><a style="color: white;text-decoration: none;" href="index.html">Home | </a></li>
                    <li><a style="color: white;text-decoration: none;" href="examples.html">Examples | </a></li>
                    <li><a style="color: white;text-decoration: none;" href="contact.html">Contact Us</a></li>
          </ul>
          <h1 align="center">Virtual Micromouse Project</h1>
          <h3 align="center">Trent Walls | Nicolas Burgess | Vivek Patel | Brian Lee</h3>
		<!--Key Start-->
       		 <div align="center" style="border: 2px solid #000; padding:4px; height:60px">
      		    <div class ="Row">
       		     <div id = "cell3"><p style="color:black;">Unknown:</p></div>
      		      <div id="cell" style="background-color:black;"></div>
      		      <div id = "cell2"><p style="color:#581845;">  Wall:</p></div>
      		      <div id="cell" style="background-color:#581845;"></div>
     		       <div id = "cell3"><p style="color:#900C3F;">  Unvisited:</p></div>
      		      <div id="cell" style="background-color:#900C3F;"></div>
      		      <div id = "cell3"><p style="color:#FF5733;">Visited:</p></div>
      		      <div id="cell" style="background-color:#FF5733;"></div>
      		      <div id = "cell3"><p style="color:#C70039;">DeadEnd:</p></div>
       		     <div id="cell" style="background-color:#C70039;"></div>
      		    </div>
       	    	</div>
       		<!--Key End-->
			<h1>Mouse 1</h1>
			<?php
			for ($y=0;$y<=32;$y++)
			{
				echo '<div class="Row">';
				for ($x=0;$x<=32;$x++)
				{	
					$map_data=mysqli_fetch_array($map_datas1);
					//echo "(".$map_data[2].",".$map_data[3].")<br>";
					$option=intval($map_data[0]);
					$type=intval($map_data[1]);
					
					if ($type==8)
					{
						echo '<div id="cell" style="background-color:black;"></div>';
					}
					else if ($type==1)
					{
						echo '<div id="cell" style="background-color:#581845;"></div>';
					}
					else
					{
						if ($option==0)
						{
							echo '<div id="cell" style="background-color:#900C3F;"></div>';
						}
						else if($option==1)
						{
							echo '<div id="cell" style="background-color:#FF5733;"></div>';
						}
						else
						{						
							echo '<div id="cell" style="background-color:#C70039;"></div>';
						}
						
					}
				}
				echo '</div>';
			}
			?>
			<br><br>
    		<h1>Mouse 2</h1>
			<?php
			for ($y=0;$y<=32;$y++)
			{
				echo '<div class="Row">';
				for ($x=0;$x<=32;$x++)
				{	
					$map_data=mysqli_fetch_array($map_datas2);
					//echo "(".$map_data[2].",".$map_data[3].")<br>";
					$option=intval($map_data[0]);
					$type=intval($map_data[1]);
					
					if ($type==8)
					{
						echo '<div id="cell" style="background-color:black;"></div>';
					}
					else if ($type==1)
					{
						echo '<div id="cell" style="background-color:#581845;"></div>';
					}
					else
					{
						if ($option==0)
						{
							echo '<div id="cell" style="background-color:#900C3F;"></div>';
						}
						else if($option==1)
						{
							echo '<div id="cell" style="background-color:#FF5733;"></div>';
						}
						else
						{						
							echo '<div id="cell" style="background-color:#C70039;"></div>';
						}
						
					}
				}
				echo '</div>';
			}
			?>
			<br><br>
			<h1>Mouse 3</h1>
			<?php
			for ($y=0;$y<=32;$y++)
			{
				echo '<div class="Row">';
				for ($x=0;$x<=32;$x++)
				{	
					$map_data=mysqli_fetch_array($map_datas3);
					//echo "(".$map_data[2].",".$map_data[3].")<br>";
					$option=intval($map_data[0]);
					$type=intval($map_data[1]);
					
					if ($type==8)
					{
						echo '<div id="cell" style="background-color:black;"></div>';
					}
					else if ($type==1)
					{
						echo '<div id="cell" style="background-color:#581845;"></div>';
					}
					else
					{
						if ($option==0)
						{
							echo '<div id="cell" style="background-color:#900C3F;"></div>';
						}
						else if($option==1)
						{
							echo '<div id="cell" style="background-color:#FF5733;"></div>';
						}
						else
						{						
							echo '<div id="cell" style="background-color:#C70039;"></div>';
						}
						
					}
				}
				echo '</div>';
			}
			?>
			<br><br>
			<h1>Mouse 4</h1>
			<?php
			for ($y=0;$y<=32;$y++)
			{
				echo '<div class="Row">';
				for ($x=0;$x<=32;$x++)
				{	
					$map_data=mysqli_fetch_array($map_datas4);
					//echo "(".$map_data[2].",".$map_data[3].")<br>";
					$option=intval($map_data[0]);
					$type=intval($map_data[1]);
					
					if ($type==8)
					{
						echo '<div id="cell" style="background-color:black;"></div>';
					}
					else if ($type==1)
					{
						echo '<div id="cell" style="background-color:#581845;"></div>';
					}
					else
					{
						if ($option==0)
						{
							echo '<div id="cell" style="background-color:#900C3F;"></div>';
						}
						else if($option==1)
						{
							echo '<div id="cell" style="background-color:#FF5733;"></div>';
						}
						else
						{						
							echo '<div id="cell" style="background-color:#C70039;"></div>';
						}
						
					}
				}
				echo '</div>';
			}
			?>

            <div class="Row">
          </div>
        </div>
    </body>
</html>
