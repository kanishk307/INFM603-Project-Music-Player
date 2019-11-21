#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

database = mysql.connector.connect(
  host="localhost",
  user="snanda1",
  passwd="snanda1006",
  database = "g4"
)
print("""
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Admin Panel</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico">
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
	<!-- to rewrite main.css -->
	<link rel="stylesheet" type="text/css" href="css/adminPanel.css">
<!--===============================================================================================-->
	<!-- JQuery -->
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<!--===============================================================================================-->
</head>
<body>
	<!-- set the first div to container of the login session -->
	<div id="add_songs_container" class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-t-50 p-b-90">
				<!-- start working with the add listeners form -->
				<form class="login100-form validate-form-login flex-sb flex-w" method = "post" action = "./updatesong.py">
					<span class="login100-form-title p-b-51">
						Add Songs to Database
					</span>
					<!-- alert if there are blank inputs-->
					<div id="error_blank_inputs" class = "limiter error_container" style='display:none'>
						<div class = "error_comment">
							*Please fill in all the required input within the form.
						</div>
					</div>

					<div class="addsongs_input_container">
						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="songname"> Song Name :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<input class="input100 add_songs_input" type="text" id="songname" name="songname">
								<span class="focus-input100"></span>
							</div>
						</div>

						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="artist"> Artist :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<select class="input100 add_songs_input" id="artist" name="artist">
""")

# fetch artist name from database
mycursor = database.cursor()
sql = "SELECT * FROM ArtistDetails"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")

print("""
								</select>
							</div>
						</div>
						
						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="album"> Album :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<input class="input100 add_songs_input" type="text" id="album" name="album">
								<span class="focus-input100"></span>
							</div>
						</div>

						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="songURL"> Song URL :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<input class="input100 add_songs_input" type="text" id="songURL" name="songURL">
								<span class="focus-input100"></span>
							</div>
						</div>

						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="imageURL"> Image URL :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<input class="input100 add_songs_input" type="text" id="imageURL" name="imageURL">
								<span class="focus-input100"></span>
							</div>
						</div>

						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="duration"> Duration :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<input class="input100 add_songs_input" type="text" id="duration" name="duration">
								<span class="focus-input100"></span>
							</div>
						</div>

						<div class="newwrap-input">
							<div class="wrap-label">
								<label for="category"> Category :</label>
							</div>
							<div class="wrap-input100 m-b-16">
								<select class="input100 add_songs_input" id="category" name="category">
""")

# fetch song category from database
sql = "SELECT * FROM Categories"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")

print("""
								</select>
							</div>
						</div>

						<div class="buttons_container">
							<div id="addsong_button" class="container-login100-form-btn-messagebox m-t-2 buttons_individual_container">
								<input class="login100-form-btn-admin" type="submit" title="Add Songs" value="ADD SONG">
							</div>

							<div  class="container-login100-form-btn-messagebox m-t-2 buttons_individual_container">
								<a id="viewsong_button" href='./songdetails.py' id="iframe_button" target="iframe_songs">
									<input name="view_songs_button" class="login100-form-btn-admin" type="button" title="View Song List" value="View Song List">
								</a>
							</div>
						</div>
					</div>

					<div class="addsongs_input_container">
						<div id="iframe_songs_container" class="iframe_songs_container">
							<iframe class = "iframe_songs" name="iframe_songs"></iframe>
						</div>
					</div>
				</form>

				<!-- start with delete listeners form -->
				<form id="delete_listeners" class="login100-form validate-form-login flex-sb flex-w" method = "post" action = "./deletelistener.py">
					<span class="login100-form-title p-b-51">
						DELETE LISTENERS
					</span>

					<div class="newwrap-input delete-listener-container">
						<div class="wrap-label delete-listeners-label">
							<label for="deletelisteners" class="delete_listener_label"> Listener Name : </label>
						</div>
						<div class="wrap-input100 m-b-16 delete-listeners-input">
							<select class="input100 add_songs_input delete-listeners-input-option" id="deletelisteners" name="deletelisteners">
""")

# fetch listeners from database
sql = "SELECT * FROM UserDetails where UserType = 'Listener'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")

print("""
							</select>
						</div>
					</div>

					<div id="delete_listeners_button" class="container-login100-form-btn-messagebox m-t-2">
						<input class="login100-form-btn-admin" type="submit" title="Delete Listeners" value="DELETE LISTENERS">
					</div>

				</form>
			</div>
		</div>
	</div>
	
<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/daterangepicker/moment.min.js"></script>
	<script src="vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<!-- import Vue before Element -->
	<script src="https://unpkg.com/vue/dist/vue.js"></script>
	<!-- import JavaScript -->
  	<script src="https://unpkg.com/element-ui/lib/index.js"></script>


	<script>
	/* ======================= using JQuery ======================= */
	/* check if the passwords don't match and show error_passwords comment */
    $(document).ready(function(){
	  $("#addsong_button").click(function(event){
	    $(".addsongs_input_container .add_songs_input").each(function( index ) {
			if ($(this).val() == '') {
	    		event.preventDefault();
	    		$("#error_blank_inputs").show();
	    		}
			}); 
	    });
	})

 	</script> 
<!--===============================================================================================-->
	<script src="js/main.js"></script>
</body>
</html>
""")