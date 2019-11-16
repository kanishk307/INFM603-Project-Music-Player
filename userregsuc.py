#!/usr/bin/python

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
userfirstname = formData.getvalue("userfirstname")
userlastname = formData.getvalue("userlastname")


import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()

print("""
<h1> User registration successful! <h1><br>
""")

verboseprint("Inserting into UserDetails database<br>")
sql = f"INSERT INTO UserDetails " + "(UserName , Password, UserFirstName, UserLastName) "\
+ f"VALUES ( \'{username}\', \'{password}\', \'{userfirstname}\', \'{userlastname}\' )"
verboseprint(f"Task insert query is {sql}")
verboseprint("<br>")
try:
  mycursor.execute(sql)
  database.commit()
except mysql.connector.Error as err:
  verboseprint("I caught an error: {}".format(err))