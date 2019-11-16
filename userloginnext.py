#!/usr/bin/python

import os
#import webbrowser

print ("Content-type: text/html")
print()

import cgi
formData = cgi.FieldStorage()

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

# For debugging purposes, define the function verboseprint.   It will print out a lot of stuff only if VERBOSE is set to true
VERBOSE = True
def verboseprint(st):
  if VERBOSE:
    print(st)
    


#grabbing variables
username = formData.getvalue("username")
password = formData.getvalue("password")

import mysql.connector


database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()

sql1 = f"SELECT Password FROM UserDetails WHERE UserName = \'{username}\'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchone()
dbpassword = myresult1[0]

sql2 = f"SELECT UserFirstName FROM UserDetails WHERE UserName = \'{username}\'"
mycursor.execute(sql2)
myresult2 = mycursor.fetchone()
userfirstname = myresult2[0]

print(f"{password}")
print(f"{dbpassword}")

#f = open(r'userloginnextpy.html','w')

if(password == dbpassword):
    print(f"{password}")
    print(f"{dbpassword}")
    message = f"""<!DOCTYPE html>
	<html>
		<head>
			<title>Songs Test Site</title>

			<!-- Include Amplitude JS -->
			<script type="text/javascript" src="js/amplitude.js"></script>
		
			<!-- Include Style Sheet -->
			<link rel="stylesheet" type="text/css" href="css/app.css"/>
			<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.bundle.min.js" integrity="sha384-feJI7QwhOS+hwpX2zkaeJQjeiwlhOP+SdQDqhgvvo1DsjtiSQByFdThsxO669S2D" crossorigin="anonymous"></script>
			<link rel="stylesheet" href="src/css/style.css" type="text/css">
			<link rel="stylesheet" href="src/css/animate.css">
		</head>
		<body class="inner-container" style="opacity:1;"> 
		<h4 style="margin-top:10%; margin-left:45%"> Hello, {userfirstname} </h4> <br>
		<input type="button"/ value="Category">
			<!-- Blue Playlist Container -->
			<div id="blue-playlist-container" style="margin-top: -7%;">
				<!-- Amplitude Player -->
				<div id="amplitude-player">

					<!-- Left Side Player -->
					
					<div id="amplitude-left">
						<img data-amplitude-song-info="cover_art_url"/>
						<div id="player-left-bottom">
							<div id="time-container">
								<span class="current-time">
									<span class="amplitude-current-minutes" ></span>:<span class="amplitude-current-seconds"></span>
								</span>
								<div id="progress-container">
									<input type="range" class="amplitude-song-slider"/>
									<progress id="song-played-progress" class="amplitude-song-played-progress"></progress>
									<progress id="song-buffered-progress" class="amplitude-buffered-progress" value="0"></progress>
								</div>
								<span class="duration">
									<span class="amplitude-duration-minutes"></span>:<span class="amplitude-duration-seconds"></span>
								</span>
							</div>

							<div id="control-container">
								<div id="repeat-container">
									<div class="amplitude-repeat" id="repeat"></div>
									<div class="amplitude-shuffle amplitude-shuffle-off" id="shuffle"></div>
								</div>

								<div id="central-control-container">
									<div id="central-controls">
										<div class="amplitude-prev" id="previous"></div>
										<div class="amplitude-play-pause" id="play-pause"></div>
										<div class="amplitude-next" id="next"></div>
									</div>
								</div>

								<div id="volume-container">
									<div class="volume-controls">
										<div class="amplitude-mute amplitude-not-muted"></div>
										<input type="range" class="amplitude-volume-slider"/>
										<div class="ms-range-fix"></div>
									</div>
									<div class="amplitude-shuffle amplitude-shuffle-off" id="shuffle-right"></div>
								</div>
							</div>

							<div id="meta-container">
								<span data-amplitude-song-info="name" class="song-name"></span>

								<div class="song-artist-album">
									<span data-amplitude-song-info="artist"></span>
									<span data-amplitude-song-info="album"></span>
								</div>
							</div>
						</div>
					</div>
					<!-- End Left Side Player -->

					<!-- Right Side Player -->
					<div id="amplitude-right">
						<!-- <div class="song amplitude-song-container amplitude-play-pause" data-amplitude-song-index="0">
							<div class="song-now-playing-icon-container">
								<div class="play-button-container">

								</div>
								<img class="now-playing" src="./img/now-playing.svg"/>
							</div>
							<div class="song-meta-data">
								<span class="song-title">Risin' High (feat Raashan Ahmad)</span>
								<span class="song-artist">Ancient Astronauts</span>
							</div>
							<a href="https://switchstancerecordings.bandcamp.com/track/risin-high-feat-raashan-ahmad" class="bandcamp-link" target="_blank">
							</a>
							<span class="song-duration">3:30</span>
						</div> -->

						
						

				<!-- End Amplitdue Player -->
			</div>
			
			
			<div class="row inner-container bg-dark">
					<div class="col bg-dark text-warning text-center" onmousedown="clickA()" onmouseup="unclickA()">
						<div data-key="65" class="beat-box my-4" id="A">
							<span class="display-4">A</span>
						 <p>Clap</p>
						</div>
						
					</div>
						
					<div class="col bg-secondary text-warning text-center" onmousedown="clickS()" onmouseup="unclickS()">
						<div data-key="83" class="beat-box my-4" id="S">
							<span class="display-4">S</span>
						 <p>Hihat</p>
						</div>
					</div>
					
					<div class="col bg-dark text-warning text-center" onmousedown="clickD()" onmouseup="unclickD()">
						<div data-key="68" class="beat-box my-4" id="D">
							<span class="display-4">D</span>
						 <p>Kick</p>
						</div>
					</div>
					
					<div class="col bg-secondary text-warning text-center" onmousedown="clickF()" onmouseup="unclickF()">
						<div data-key="70" class="beat-box my-4" id="F">
							<span class="display-4">F</span>
						 <p>Open hat</p>
						</div>
					</div>
					
					<div class="col bg-dark text-warning text-center" onmousedown="clickG()" onmouseup="unclickG()">
						<div data-key="71" class="beat-box my-4" id="G">
							<span class="display-4">G</span>
						 <p>Boom</p>
						</div>
					</div>
					
					<div class="col bg-seconda3ry text-warning text-center" onmousedown="clickH()" onmouseup="unclickH()">
						<div data-key="72" class="beat-box my-4" id="H">
							<span class="display-4">H</span>
						 <p>Ride</p>
						</div>
					</div>
					
					<div class="col bg-dark text-warning text-center" onmousedown="clickJ()" onmouseup="unclickJ()">
						<div data-key="74" class="beat-box my-4" id="J">
							<span class="display-4">J</span>
						 <p>Snare</p>
						</div>
					</div>
					
					<div class="col bg-secondary text-warning text-center" onmousedown="clickK()" onmouseup="unclickK()">
						<div data-key="75" class="beat-box my-4" id="K">
							<span class="display-4">K</span>
						 <p>Tom</p>
						</div>
					</div>
					
					<div class="col bg-dark text-warning text-center" onmousedown="clickL()" onmouseup="unclickL()">
						<div data-key="76" class="beat-box my-4" id="L">
							<span class="display-4">L</span>
						 <p>Tink</p>
						</div>
					</div>


					<audio data-key="65" src="src/sounds/clap.wav"></audio>
					<audio data-key="83" src="src/sounds/hihat.wav"></audio>           
					<audio data-key="68" src="src/sounds/kick.wav"></audio> 
					<audio data-key="70" src="src/sounds/openhat.wav"></audio>
					<audio data-key="71" src="src/sounds/boom.wav"></audio>            
					<audio data-key="72" src="src/sounds/ride.wav"></audio>           
					<audio data-key="74" src="src/sounds/snare.wav"></audio>   
					<audio data-key="75" src="src/sounds/tom.wav"></audio>  
					<audio data-key="76" src="src/sounds/tink.wav"></audio>   

			<!--
				Include UX functions JS

				NOTE: These are for handling things outside of the scope of AmplitudeJS
			-->
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
			<script type="text/javascript" src="js/functions.js"></script>
			<script type="text/javascript" src="data.json"></script>
			<script src="src/js/script.js"></script>
			<script src="src/js/wow.min.js"></script>
			<!-- <script type="text/javscript" src="js/amplitude.js"></script> -->
		</body>
	</html>
	"""
    print(message)
    
else:
    print("That")

"""
verboseprint(f"Task insert query is {sql}")
verboseprint("<br>")
try:
  mycursor.execute(sql)
  database.commit()
except mysql.connector.Error as err:
  verboseprint("I caught an error: {}".format(err))
 """ 
 
