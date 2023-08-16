from markupsafe import escape
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER= "/Up/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
carpeta = "src/static/uploads/"


@app.route("/")
def login():
   return render_template("login.html")

@app.route("/dashboard")
def menu():
   return render_template("dashboard.html")

@app.route("/files")
def files():
   #   return """<a href="http://localhost:5000/view/"""+archivo+"""">"""+archivo+"""</a>"""
   #return """<p>"""+archivo+"""</p>"""
   contenido = os.listdir(carpeta)
   result_str = ", ".join(contenido)
   return """
      <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/files.css">
    <title>Archivos</title>
    <script defer src="../static/js/files.js"></script>
</head>
<body>
    <h1>Archivos guardados en el servidor</h1>
    <p>Archivos: """+ result_str +"""</p>
    <div class="input">
        <h2>Abrir archivo</h2>
        <input id="input" type="text">
        <button id="button">Abrir</button>
    </div>
</body>
</html>
"""
   
   

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file(): 
   if request.method == 'POST':
      f = request.files['file']
      name=secure_filename(f.filename)
      f.save(carpeta+name)
      return """<nav style="display: flex;align-items: center;background-color: #777; width: 100vw; height: 10vh;"><h1>MarkBase</h1><p>"""+name+"""</p><a href="http://localhost:5000/dashboard">Menu</a><a href="http://localhost:5000/static/uploads/"""+name+"""" download="proposed_file_name">Download</a></nav><iframe style="width: 100vw;" height="90%" id="iframe" src="http://localhost:5000/static/uploads/""" +name+"""" frameborder="0"></iframe><style>*{overflow-y: hidden; overflow-x: hidden;}body{margin:0;}nav *{margin-left: 20px;}</style>"""

@app.route("/view/<name>")
def view(name):
   if name.endswith(".docx"):
      print(".docx")
      return """<nav style="display: flex;align-items: center;background-color: #777; width: 100vw; height: 10vh;"><h1>MarkBase</h1><p>"""+name+"""</p><a href="http://localhost:5000/dashboard">Menu</a><a href="http://localhost:5000/static/uploads/"""+name+"""" download="proposed_file_name">Download</a></nav><iframe src="https://docs.google.com/gview?url=http://192.168.1.40:5000/static/uploads/"""+name+"""&embedded=true"></iframe><style>*{overflow-y: hidden; overflow-x: hidden;}body{margin:0;}nav *{margin-left: 20px;}iframe{width: 90vw;height: 100vh;}</style>"""
   else:
      return """<nav style="display: flex;align-items: center;background-color: #777; width: 100vw; height: 10vh;"><h1>MarkBase</h1><p>"""+name+"""</p><a href="http://localhost:5000/dashboard">Menu</a><a href="http://localhost:5000/static/uploads/"""+name+"""" download="proposed_file_name">Download</a></nav><iframe style="width: 100vw;" height="90%" id="iframe" src="http://localhost:5000/static/uploads/""" +name+"""" frameborder="0"></iframe><style>*{overflow-y: hidden; overflow-x: hidden;}body{margin:0;}nav *{margin-left: 20px;}</style>"""
   

if __name__ == '__main__':
   app.run(debug = True)