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
    


#grabbing variables
username = formData.getvalue("username")
password = formData.getvalue("password")

import mysql.connector


database = mysql.connector.connect(
  host="localhost",
  user="kjain307",
  passwd="kjain307873",
  database = "g4"
)

mycursor = database.cursor()

sql = f"SELECT Password FROM UserDetails WHERE UserName = \'{username}\' AND UserType = \'Admin\'"
mycursor.execute(sql)
myresult = mycursor.fetchone()



if myresult is None: # if the username isn't in the database or the usertype isn't Admin
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
                  That email and password combination is incorrect
                </span>

                <div class="limiter">
                  <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                    <a href='./adminlogin.html'>
                      <input name="admin" class="login100-form-btn-messagebox" style="background-color: #e35b61; margin-bottom: 5%;" type="button" value="Try Again!">
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
else:
  dbpassword = myresult[0] # if the Admin username is valid, then check the password
  if (password == dbpassword):
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
                {username}, you are heading to the Admin Panel page!
              </span>

              <div class="limiter">
                <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                  <a href='./adminPanel.py'>
                    <input name="admin" class="login100-form-btn-messagebox" style="background-color: #4685c0; margin-bottom: 5%;" type="button" value="Go ahead!">
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
                      That email and password combination is incorrect
                    </span>

                    <div class="limiter">
                      <div class="container-login100-form-btn-messagebox m-t-17" style="width:100%; margin:0px auto;">
                        <a href='./adminlogin.html'>
                          <input name="admin" class="login100-form-btn-messagebox" style="background-color: #e35b61; margin-bottom: 5%;" type="button" value="Try Again!">
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