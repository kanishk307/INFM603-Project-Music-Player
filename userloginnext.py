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
	<html style="background-color:black;">
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
			 <link rel="stylesheet" type="text/css" href="css/recstyle.css">
			 <meta name="viewport" content="width=device-width, initial-scale=1.0">
		</head>
		<body class="inner-container" style="opacity:1;"> 
		<h4 style="margin-top:10%; margin-left:45%"> Hello, {userfirstname} </h4> 
		<div> 

		<!--<div>
		<iframe src="recording.html" width=600 height=200  name="recorder"></iframe>
		</div>
		-->
		
		<!--
		<div id="rec">
			   <div id="controls">
			 <button id="recordButton">Record</button>
			 <button id="pauseButton" disabled>Pause</button>
			 <button id="stopButton" disabled>Stop</button>
			</div>
			<div id="formats">Format: start recording to see sample rate</div>
			<h3>Recordings</h3>
			<ol id="recordingsList"></ol>

		</div>
		-->

		<div style="text-align:center;"> <h3><a href="testmusicplaymain.py" target="iframe_allsongs">All Songs</a> || <a href="testmusicplayerhiphop.py" target="iframe_allsongs">Hip Hop</a>
		||  <a href="testmusicplayerreggae.py" target="iframe_allsongs">Reggae</a> ||  <a href="testmusicplayerrnb.py" target="iframe_allsongs">RNB</a>
		||  <a href="testmusicplayerrock.py" target="iframe_allsongs">Rock</a> ||  <a href="testmusicplayerpop.py" target="iframe_allsongs">Pop</a>
		</h3>   </div>
			<!-- Blue Playlist Container -->
			<iframe src="testmusicplaymain.py" width=1050 height=1000 style="margin-top:2%; margin-left: 7%" name="iframe_allsongs"></iframe>
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
					
					<div class="col bg-secondary text-warning text-center" onmousedown="clickH()" onmouseup="unclickH()">
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
			<script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
  			<script type="text/javascript" src="js/recorder.js"></script>
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
 
