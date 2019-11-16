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
<form method = "post" action = "http://kjain307.psjconsulting.com/Project/updatesong.py">
Song Name : <input type=\"text\" name=\"songname\"> 
<br>
""")



print("""
Artist Name :
<select name = \"artistname\">
""")

mycursor = database.cursor()

sql = "SELECT * FROM ArtistDetails"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")
print("""
</select>
<br>
""")


print("""
Song URL : <input type=\"text\" name=\"songurl\"> 
<br>
""")

print("""
Image URL : <input type=\"text\" name=\"imageurl\"> 
<br>
""")


print("""
Song Duration : <input type=\"text\" name=\"songduration\"> 
<br>
""")



print("""
Category Name :
<select name = \"songcategoryname\">
""")
sql = "SELECT * FROM Categories"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")
print("""
</select>
<br>
""")




print("""
<<<<<<< HEAD
<input type="submit" value="SUBMIT">
=======
<input type="submit" value="submit">
>>>>>>> 926cd89f6743cccbc91c9f35bd577c68135d8023
</form>""")
  
