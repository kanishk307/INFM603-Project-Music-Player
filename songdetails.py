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
sql = f"SELECT * FROM Songs"

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(f"""<h2> Songs List </h2>
<table>
<tr>
<td>SongName</td>
<td>Artist</td>
<td>Album</td>
<td>Duration</td>
</tr>""")
for x in myresult :
  print(f"""<tr>
  <td>{x[1]}</td>
  <td>{x[2]}</td>
  <td>{x[3]}</td>
  <td>{x[6]}</td> 
  </tr>""")
  
print("""
</table>
""")

