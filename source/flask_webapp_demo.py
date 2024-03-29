from flask import Flask
from flask_cors import CORS

import sqlite3
from sqlite3 import Error

import json

app = Flask( __name__ )
CORS( app )

@app.route( "/" )
def home():
  res = "Hello World! This is my first Flask web app."
  return res

# Static routing
@app.route( "/greet/RVU" )
def greetRVU():
  return "Hi RVU! Welcome.  We are glad you are here.  How are you today?"

# Dyanmic routing with "Name" as parameter - default data type is string
@app.route( "/greet/<Name>", methods = [ "GET" ] )
def greet( Name ):
  res = "Hi " + Name + "! We are glad you are here.  How are you today?"
  return res

@app.route ("/getDetails/<Name>", methods = [ "GET" ] )
def getDetails( Name ):

  try:

    conn = sqlite3.connect( "students.db" )
    cur = conn.cursor()

    if ( Name == "*" ):
      query = "SELECT * FROM students ORDER BY USN"
    else:
      query = "SELECT * FROM students WHERE Name LIKE \"%" + Name + "%\" ORDER BY USN"
    print( query )

    cur.execute( query )
    row = cur.fetchall()
    print( row )

    conn.close()

    return( json.dumps( row ) )
  
  except Error as e:
    return( "Error while trying to query students.db: " + str( e ) )

if __name__ == "__main__":
  app.run( port = 9001 )