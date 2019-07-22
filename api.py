from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder="./app/static", template_folder="./app/templates")
app.config["DEBUG"] = True
CORS(app)

# View Routes
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

# Dining Room
@app.route('/api/zone/dining/on', methods=['GET'])
def dining_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/dining/off', methods=['GET'])
def dining_off():
  return 'Replace this line with your code!'

@app.route('/api/zone/dining/up', methods=['GET'])
def dining_up():
  return 'Replace this line with your code!'

@app.route('/api/zone/dining/down', methods=['GET'])
def dining_down():
  return 'Replace this line with your code!'

# Living Room
@app.route('/api/zone/living/on', methods=['GET'])
def living_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/living/off', methods=['GET'])
def living_off():
  return 'Replace this line with your code!'

@app.route('/api/zone/living/up', methods=['GET'])
def living_up():
  return 'Replace this line with your code!'

@app.route('/api/zone/living/down', methods=['GET'])
def living_down():
  return 'Replace this line with your code!'

# Bathrooms
@app.route('/api/zone/bathrooms/on', methods=['GET'])
def bathrooms_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/bathrooms/off', methods=['GET'])
def bathrooms_off():
  return 'Replace this line with your code!'

@app.route('/api/zone/bathrooms/up', methods=['GET'])
def bathrooms_up():
  return 'Replace this line with your code!'

@app.route('/api/zone/bathrooms/down', methods=['GET'])
def bathrooms_down():
  return 'Replace this line with your code!'

# Master
@app.route('/api/zone/master/on', methods=['GET'])
def master_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/master/off', methods=['GET'])
def master_off():
  return 'Replace this line with your code!'

@app.route('/api/zone/master/up', methods=['GET'])
def master_up():
  return 'Replace this line with your code!'

@app.route('/api/zone/master/down', methods=['GET'])
def master_down():
  return 'Replace this line with your code!'

# Outside
@app.route('/api/zone/outside/on', methods=['GET'])
def outside_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/outside/off', methods=['GET'])
def outside_off():
  return 'Replace this line with your code!'

@app.route('/api/zone/outside/up', methods=['GET'])
def outside_up():
  return 'Replace this line with your code!'

@app.route('/api/zone/outside/down', methods=['GET'])
def outside_down():
  return 'Replace this line with your code!'

# Globals
@app.route('/api/zone/global/on', methods=['GET'])
def global_on():
  return 'Replace this line with your code!'

@app.route('/api/zone/global/off', methods=['GET'])
def global_off():
  return 'Replace this line with your code!'

app.run()