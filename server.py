from flask import Flask, send_file

# import other repository files
import website.server as websiteProject
import my_cool_app.server as myCoolApplication

app = Flask(__name__)

@app.route('/')
def rootPath():
  return "You're at root!"

@app.route('/json')
def jsonRoute():
  return send_file('sample.json')

# pass in flask instance to allow extensions
websiteProject.extendApplication(app)
myCoolApplication.extendApplication(app)
