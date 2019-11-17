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
<input type="submit" value="SUBMIT"> <strong> <a href="songdetails.py" target="iframe_songs">Songs List</a> <strong>
</form>""")
  
print("""
<iframe height="300px" width="100%" src="" name="iframe_songs"></iframe>  
""") 

#Embed Delete Listener Functionality for the ADMIN
  
print("""
<form method = "post" action = "http://snanda1.psjconsulting.com/deletelistener.py">
<h2>DELETE LISTENERS
</h2>""")
  
print("""
Listener Name :
<select name = \"username\">
""")
sql = "SELECT * FROM UserDetails where UserType = 'Listener'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(f"<option>{x[1]}</option>")
    
print("""
</select> 
<input type="submit" value="DELETE">
</form>""")

