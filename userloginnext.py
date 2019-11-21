#!/usr/bin/python

import os

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

sql = f"SELECT Password FROM UserDetails WHERE UserName = \'{username}\' AND UserType = \'Listener\'"
mycursor.execute(sql)
myresult = mycursor.fetchone()

sql2 = f"SELECT UserFirstName FROM UserDetails WHERE UserName = \'{username}\' AND UserType = \'Listener\'"
mycursor.execute(sql2)
myresult2 = mycursor.fetchone()
#firstname = myresult2[0] can't write it here bc there will be 404 if we couldn't find the user

if myresult is None: # if the username isn't in the database or the usertype isn't Listener
  print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Message Page</title>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->  
      <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
    <!--===============================================================================================-->  
      <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
    <!--===============================================================================================-->  
      <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
    <!--===============================================================================================-->
      <!-- Add vue resources below -->
      <!-- import CSS -->
      <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="css/util.css">
      <link rel="stylesheet" type="text/css" href="css/main.css">
    <!--===============================================================================================-->
    </head>

    <body>
      <div id="login_admin" class="limiter">
        <div class="container-login100">
          <div class="wrap-login100-messagebox p-t-50 p-b-0" style="border: 2px solid #e97085;padding-left: 5%; padding-right: 5%;">
            <div id="messagebox" class="m-b-16">
              <span class="login100-form-title-messagebox p-b-25" style="color: #d94a57">
                That email and password combination is incorrect
              </span>

              <div class="limiter">
                <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                  <a href='./userlogin.html'>
                    <input name="listener" class="login100-form-btn-messagebox" style="background-color: #e35b61; margin-bottom: 5%;" type="button" value="Try Again!">
                  </a>
                </div>
              </div>
                
            </div>
          </div>
        </div>
      </div>

    </body>
    </html>
    """)
else:
  dbpassword = myresult[0] # if the Listener username is valid, then check the password
  firstname = myresult2[0] # bring the selected firstname here
  if (password == dbpassword):
    message = f"""<!DOCTYPE html>
    <html style="background-color:#c5c5fa;">
      <head>
        <title>Songs Page</title>
        <!-- Include Amplitude JS -->
        <script type="text/javascript" src="js/amplitude.js"></script>
      
        <!-- Include Style Sheet -->
        <link rel="stylesheet" type="text/css" href="css/app.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.bundle.min.js" integrity="sha384-feJI7QwhOS+hwpX2zkaeJQjeiwlhOP+SdQDqhgvvo1DsjtiSQByFdThsxO669S2D" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="src/css/style.css" type="text/css">
        <link rel="stylesheet" href="src/css/animate.css">
         <link rel="stylesheet" type="text/css" href="css/recstyle.css">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
      </head>

      <body class="inner-container" style="background:#000000; color:#ffffff; border: 10px solid #827ffe"> 
	  
	  <!#################### NAVBAR ##################################>
	  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Howdy, {firstname}! &#127932;</a>
 

  <div class="collapse navbar-collapse" id="navbarSupportedContent" style="margin-left:18%;">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="testmusicplaymain.py" target="iframe_allsongs">All Songs <span class="sr-only"></span></a>
      </li>
	   <li class="nav-item active">
        <a class="nav-link" href="testmusicplayerhiphop.py" target="iframe_allsongs">Hip Hop<span class="sr-only"></span></a>
      </li>
	   <li class="nav-item active">
        <a class="nav-link" href="testmusicplayerreggae.py" target="iframe_allsongs">Reggae<span class="sr-only"></span></a>
      </li>
	   <li class="nav-item active">
        <a class="nav-link" href="testmusicplayerrnb.py" target="iframe_allsongs">RNB<span class="sr-only"></span></a>
      </li>
	  <li class="nav-item active">
        <a class="nav-link" href="testmusicplayerrock.py" target="iframe_allsongs">Rock<span class="sr-only"></span></a>
      </li>
	 <li class="nav-item active">
        <a class="nav-link" href="testmusicplayerpop.py" target="iframe_allsongs">Pop<span class="sr-only"></span></a>
      </li>
	</ul>
  </div>
</nav>

<!-- #######################################################NAVBAR#############################################333 -->
	  
        <h3 style="text-align:center; margin-top:1.5%; ">&#127925; BEATS PLEASE &#127925;</h3> 
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
       <!-- <div style="text-align:center;"> 
          <h3><a href="testmusicplaymain.py" target="iframe_allsongs">All Songs</a> || <a href="testmusicplayerhiphop.py" target="iframe_allsongs">Hip Hop</a>
          ||  <a href="testmusicplayerreggae.py" target="iframe_allsongs">Reggae</a> ||  <a href="testmusicplayerrnb.py" target="iframe_allsongs">RNB</a>
          ||  <a href="testmusicplayerrock.py" target="iframe_allsongs">Rock</a> ||  <a href="testmusicplayerpop.py" target="iframe_allsongs">Pop</a>
          </h3>   
        </div> -->
		
		<div style="text-align: center; margin-top:3%; color:black;">
		<strong>&#129345; Compose your beats &#129345;</strong>
		</div>

        <!-- Blue Playlist Container -->
        <iframe src="testmusicplaymain.py" width=1200 height=1000 style="margin-top:15%; margin-left: -1%; border-radius:10px;" name="iframe_allsongs"></iframe>
		
   
		<div class="row inner-container" style="border-radius:10px;margin-top:12%;">

            <div class="col bg-dark text-warning text-center" onmousedown="clickA()" onmouseup="unclickA()" style="border-radius:10px 0 0 10px;">
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
            
            <div class="col bg-dark text-warning text-center" onmousedown="clickL()" onmouseup="unclickL()" style="border-radius:0 10px 10px 0;">
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
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Message Page</title>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->  
      <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
    <!--===============================================================================================-->  
      <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
    <!--===============================================================================================-->  
      <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
    <!--===============================================================================================-->
      <!-- Add vue resources below -->
      <!-- import CSS -->
      <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
    <!--===============================================================================================-->
      <link rel="stylesheet" type="text/css" href="css/util.css">
      <link rel="stylesheet" type="text/css" href="css/main.css">
    <!--===============================================================================================-->
    </head>

    <body>
      <div id="login_admin" class="limiter">
        <div class="container-login100">
          <div class="wrap-login100-messagebox p-t-50 p-b-0" style="border: 2px solid #e97085;padding-left: 5%; padding-right: 5%;">
            <div id="messagebox" class="m-b-16">
              <span class="login100-form-title-messagebox p-b-25" style="color: #d94a57">
                That email and password combination is incorrect
              </span>

              <div class="limiter">
                <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                  <a href='./userlogin.html'>
                    <input name="listener" class="login100-form-btn-messagebox" style="background-color: #e35b61; margin-bottom: 5%;" type="button" value="Try Again!">
                  </a>
                </div>
              </div>
                
            </div>
          </div>
        </div>
      </div>
    </body>
    </html>
  """)