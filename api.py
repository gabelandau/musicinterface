from flask import Flask, render_template

app = Flask(__name__, static_folder="./app/static", template_folder="./app/templates")
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

app.run()