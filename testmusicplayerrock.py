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
    


import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()


htmlplayer = f"""<!DOCTYPE html>
	<html style="">
		<head>
			<title>Rock</title>

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
		<body class="inner-container iframe-container" style="opacity:1;background:#000000 ;color:#827ffe;"> 
		<h3 style="text-align:center; margin-top: -10%;"> Rock </h3>
			<!-- Blue Playlist Container -->
			<div id="blue-playlist-container" style="margin-top: -10%;">
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
								
						</div> -->

						
						

				<!-- End Amplitdue Player -->
			</div>
						<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
			<script type="text/javascript" src="js/functions-rock.js"></script>
			<script type="text/javascript" src="data.json"></script>
			<script src="src/js/script.js"></script>
			<script src="src/js/wow.min.js"></script>
			<!-- <script type="text/javscript" src="js/amplitude.js"></script> -->
			</body>
	</html>"""

print(htmlplayer)			