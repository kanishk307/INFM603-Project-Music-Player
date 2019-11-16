#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)




print("""
<h1> User Registration </h1>
<form method = "post" action = "./userregsuc.py">
Username (Email) : <input type=\"email\" name=\"username\"> 
<br>
Password : <input type=\"password\" name=\"password\"> 
<br>
First Name : <input type=\"text\" name=\"userfirstname\"> 
<br>
Last Name : <input type=\"text\" name=\"userlastname\"> 
<br>
""")






print("""
<input type="submit" value="submit">
</form>""")
  
