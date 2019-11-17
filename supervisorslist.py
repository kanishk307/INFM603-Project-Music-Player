#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "kjain307_hw8"
)
mycursor = database.cursor()
sql = "Select * FROM Supervisor"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(f"""<h2> Supervisors List </h2>
<table><tr>
<td>Supervisor id </td>
<td>Supervisor First Name </td>
<td>Supervisor Last Name </td>
<td>Supervisor Title </td>
<td>Supervisor phone extension </td>
</tr>""")
for x in myresult :
  print (f"""<tr>
  <td>{x[0]}</td>
  <td>{x[1]}</td>
  <td>{x[2]}</td>
  <td>{x[3]}</td>
  <td>{x[4]}</td>
  </tr>""")
print(f"""
</table>
""")
	  