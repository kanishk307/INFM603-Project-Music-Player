#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()
sql = f"""Select * FROM Songs"""

sql2 = f"""SELECT '[' """



mycursor.execute(sql)
myresult = mycursor.fetchall()
print(f"""<h2> Songs List </h2>
<table><tr>
<td>Song ID </td>
<td>Song Name</td>
<td>Artist</td>
<td>Album</td>
<td>Song Duration</td>
</tr>""")
for x in myresult :
  print (f"""<tr>
  <td>{x[0]}</td>
  <td>{x[1]}</td>
  <td>{x[2]}</td>
  <td>{x[3]}</td>
  <td>{x[6]}</td>
  </tr>""")
print(f"""
</table>
""")


mycursor.execute(sql2)
myresult2 = mycursor.fetchall()
for x in myresult2:
	print(f"""x
	""")