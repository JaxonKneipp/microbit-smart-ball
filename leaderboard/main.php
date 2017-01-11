<?php

$servername = "localhost";
$username = "seansweb_ncss";
$password = "jaXon";
$databaseName = "seansweb_ncssProject";

// Create connection
$conn = new mysqli($servername, $username, $password, $databaseName);

// Check connection
if ($conn->connect_error) {

    die("Connection failed: " . $conn->connect_error);
	
} 

$action = $_GET["action"];

if ($action == "c") {

	// CREATE NEW GAME
	
	$gamename = $_GET["gamename"];
	
	$sql = "INSERT INTO games (game_name, count) VALUES ('".$gamename."', 0)";

	if ($conn->query($sql) === TRUE) {
	
		echo "New record created successfully";
		
	} else {
	
		echo "Error: " . $sql . "<br>" . $conn->error;
		
	}	
	
} else if ($action == "i") {
		
	$gamename = $_GET["gamename"];
	
	$sql = "UPDATE games SET count = count + 1 WHERE game_name = '".$gamename."'";

	if ($conn->query($sql) === TRUE) {
	
		echo "Incrementation complete";
		
	} else {
	
		echo "Error: " . $sql . "<br>" . $conn->error;
		
	}	
	
} else if ($action == "d") {
		
	$gamename = $_GET["gamename"];
	
	$sql = "SELECT * FROM games WHERE game_name='".$gamename."'";
	
	$result = $conn->query($sql);
	
	if ($result->num_rows > 0) {
		
		while($row = $result->fetch_assoc()) {
			
			echo "<html>

					<head>
					
						<title>
						
							Smart Soccer ball
						
						</title>
						
						<meta http-equiv='refresh' content='1'>
						
						<link href='https://fonts.googleapis.com/css?family=Inconsolata' rel='stylesheet'>
						
						<style>
						
							body {
							
								text-align: center;
								font-family: 'Inconsolata', monospace;
							
							}
						
							#score {
								
								margin-top: 30%;
								font-size: 300px;
							
							}
						
						</style>
					
					</head>
					
					<body>
					
						<h1 id='score'>".$row["count"]."</h1>
					
					</body>

				</html>
				";
						
		}
		
	}
}
	
?>