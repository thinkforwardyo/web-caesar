from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="POST">
      Rotate by:<input type="text" name="rot" value="0">
      <textarea name="text">{0}</textarea>
      <button name="submit">Submit</button>
      
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')
@app.route("/",methods=['Post'])
def encrypt(text,keyword):
    rot = int(request.form.get("rot"))
    text = str(request.form.get("text"))
    encrypted_msg = rotate_string(text,rot)
    return form.format(encrypted_msg)

app.run()