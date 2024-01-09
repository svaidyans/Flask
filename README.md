<p align="center">
  <img src="images/flask.png" width="110" height="125"></img>
</p>

# Full stack Web and Desktop app development with Flask
I am teaching Computer Science courses to 1st year under-grad students pursuing Bachelor of Technology.

A course being taught is *_"Building Apps with Python"_*.  One of the course outcome is to equip students with knowledge of creating a minimalist web app and a desktop app.  Being a micro web framework with built-in web server and with its capability to allow reuse of 99% of the codebase for creating a web app as well as desktop app (targeting both Windows and Mac), Flask is the ideal choice for this use case.

For developing desktop apps, we will be using the FlaskWebGui package.

## App requirements
The intention is search for and retrieve student(s) information like Name, Email, Batch, USN, ID, Section stored in a database and display in a table.  A wireframe is as below:
<p align="center">
  <img src="images/sis.png"></img>
</p>

## Software stack
- Python 3.9
- Flask 2.2.3
- Flask-Cors 3.0.10
- flaskwebgui 1.0.8
- SQLite3
- HTML, CSS, JavaScript, RESTful API

## Source Code
The [source](https://github.com/svaidyans/Flask/tree/main/source) folder contains the Python and HTML code.

## Desktop Apps
Another advantage of developing desktop app with Flask (using package FlaskWebGui) is that it just spawns a new flask server thread with a browser - so the look and feel is same as web app (and for Windows, avoids the DLL hell).  The desktop apps are available in the [desktop](https://github.com/svaidyans/Flask/tree/main/dapps) folder.  

