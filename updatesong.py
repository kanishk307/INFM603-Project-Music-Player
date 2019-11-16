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
artistname = formData.getvalue("artistname")
songurl = formData.getvalue("songurl")
imageurl = formData.getvalue("imageurl")
songduration = formData.getvalue("songduration")
songcategoryname = formData.getvalue("songcategoryname")


sql1 = f"SELECT Artist_ID FROM ArtistDetails WHERE ArtistName = \'{artistname}\'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchone()
artistid = myresult1[0]

<<<<<<< HEAD
sql2 = f"SELECT Category_ID FROM Categories WHERE Category_type= \'{songcategoryname}\'"
mycursor.execute(sql2)
myresult2 = mycursor.fetchone()
categoryid = myresult2[0]

verboseprint(f"Artist id is {artistid} and Category id is {cateogoryid}")


=======
sql2 = f"SELECT Category_ID FROM Categories WHERE Category_type = \'{songcategoryname}\'"
mycursor.execute(sql2)
myresult2=mycursor.fetchone()
songcategoryid = myresult2[0]

print(f"{artistid} {songcategoryid}")

#SQL POST TO DATABASE
verboseprint("Inserting into SongDetails database<br>")
sql = f"INSERT INTO SongDetails " + "(SongName , Artist_ID, SongURL, ImageURL, SongDuration, Category_ID) "\
+ f"VALUES ( \'{songname}\', \'{str(artistid)}\', \'{songurl}\', \'{imageurl}\', \'{songduration}\', \'{str(songcategoryid)}\' )"
verboseprint(f"Task insert query is {sql}")
verboseprint("<br>")
try:
  mycursor.execute(sql)
  database.commit()
except mysql.connector.Error as err:
  verboseprint("I caught an error: {}".format(err))
>>>>>>> 926cd89f6743cccbc91c9f35bd577c68135d8023
