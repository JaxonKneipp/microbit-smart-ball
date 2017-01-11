<?php

$servername = "localhost";
$username = "seansweb_ncss";
$password = "jaXon";
$databaseName = "seansweb_ncssProject";

$conn = new mysqli($servername, $username, $password, $databaseName);

if ($conn->connect_error) {

    die("Connection failed: " . $conn->connect_error);
	
} 	

$gamename = $_GET["gamename"];

$sql = "SELECT * FROM games ORDER BY count DESC";

$result = $conn->query($sql);

echo "<html><head><meta http-equiv='refresh' content='1'><link href='https://fonts.googleapis.com/css?family=Inconsolata' rel='stylesheet'>
</head><body style='font-family: \"Inconsolata\", monospace;'><br/><br/><h1 style='text-align:center;'>SMART BALL</h1><h2 style='text-align:center;'>LEADERBOARD</h2><br/>";

if ($result->num_rows > 0) {
	
	echo '<ol>';
		
	while($row = $result->fetch_assoc()) {
					
		echo '<li><strong>'.$row["game_name"]."</strong> has the score <strong>".$row["count"]."</strong></li>";
		
	}
	
	echo "</ol>";
	
}

echo "</body></html>";
	
?>