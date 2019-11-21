#!/usr/bin/python

import os
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

#--------grabbing variables---------
# from the register form
firstname = formData.getvalue("firstname")
lastname = formData.getvalue("lastname")
username = formData.getvalue("username")
password = formData.getvalue("password")
password_confirm = formData.getvalue("password_confirm")

import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()

# need to check whether the email already exists
# also need to check whether the password match with password_confirm

sql = f"SELECT * FROM UserDetails WHERE UserName = \'{username}\' AND UserType = \'Listener\'"
mycursor.execute(sql)
myresult = mycursor.fetchone()

if myresult is None: # check if the username is already in the database
  # insert user info into the database
  sql = f"INSERT INTO UserDetails " + "(UserName , Password, UserFirstName, UserLastName) "\
  + f"VALUES ( \'{username}\', \'{password}\', \'{firstname}\', \'{lastname}\' )"
  try:
    mycursor.execute(sql)
    database.commit()
    print("""
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
                  You successfully registered!
                </span>

                <div class="limiter">
                  <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                    <a href='./userlogin.html'>
                      <input name="listener" class="login100-form-btn-messagebox" style="background-color: #4685c0; margin-bottom: 5%;" type="button" value="Go back and log in!">
                    </a>
                  </div>
                </div>
                  
              </div>
            </div>
          </div>
        </div>

      </body>
      </html>
      """)
  except mysql.connector.Error as err:
    verboseprint("I caught an error: {}".format(err))
# when the username already exists in database
else:
  print("""
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
          <div class="wrap-login100-messagebox p-t-50 p-b-0" style="border: 2px solid #e97085;padding-left: 5%; padding-right: 5%;">
            <div id="messagebox" class="m-b-16">
              <span class="login100-form-title-messagebox p-b-25" style="color: #d94a57">
                The Email has already been registered
              </span>

              <div class="limiter">
                <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                  <a href='./userlogin.html'>
                    <input name="listener" class="login100-form-btn-messagebox" style="background-color: #e35b61; margin-bottom: 5%;" type="button" value="Try Again!">
                  </a>
                </div>
              </div>
                
            </div>
          </div>
        </div>
      </div>

    </body>
    </html>
  """)
