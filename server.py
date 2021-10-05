from mods.config import *
from flask import Flask, render_template, request, redirect, url_for
from mysqlconnection import MySQLConnection
import os
from parseCSV import parseCSV

app = Flask(__name__)
app.secret_key = 'dontevenneedit'

# Upload folder
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route("/")
def index():
    # Set The upload HTML template './templates/index.html'
    return render_template("index.html")

# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        parseCSV(file_path)
        # save the file
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)