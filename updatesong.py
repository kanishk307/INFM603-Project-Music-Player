#!/usr/bin/python

print ("Content-type: text/html")
print()

# Get the data from the form
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

songname = formData.getvalue("songname")
artistname = formData.getvalue("artist")
album = formData.getvalue("album")
url = formData.getvalue("songURL")
cover_art_url = formData.getvalue("imageURL")
duration = formData.getvalue("duration")
songcategoryname = formData.getvalue("category")


sql1 = f"SELECT Artist_ID FROM ArtistDetails WHERE ArtistName = \'{artistname}\'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchone()
artistid = myresult1[0]

sql2 = f"SELECT Category_ID FROM Categories WHERE Category_type = \'{songcategoryname}\'"
mycursor.execute(sql2)
myresult2=mycursor.fetchone()
songcategoryid = myresult2[0]


#SQL POST TO DATABASE
# insert data into the SongDetails table
sql1 = f"INSERT INTO Songs " + "(name , artist, album, url, cover_art_url,duration, Category_ID) "\
+ f"VALUES ( \'{songname}\', \'{artistname}\', \'{album}\', \'{url}\', \'{cover_art_url}\',\'{duration}\', \'{str(songcategoryid)}\' )"

try:
  mycursor.execute(sql1)
  database.commit()
  content = f"""
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
				<div class="wrap-login100-messagebox p-t-50 p-b-0" style="border: 2px solid #709bd7;padding-left: 5%; padding-right: 5%;">
					<div id="messagebox" class="m-b-16">
						<span class="login100-form-title-messagebox p-b-25" style="color: #5d82c6;">
							The Song "{songname}" by {artistname} has successfully been added!
						</span>

						<div class="limiter">
							<div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
								<a href='./adminPanel.py'>
									<input name="listener" class="login100-form-btn-messagebox" style="background-color: #4685c0; margin-bottom: 5%;" type="button" value="Go back!">
								</a>
							</div>
						</div>
							
					</div>
				</div>
			</div>
		</div>

	</body>
	</html>
  """
  print(content)
except mysql.connector.Error as err:
  verboseprint("I caught an error: {}".format(err))
