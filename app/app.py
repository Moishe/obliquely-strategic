import os

from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'obliquely-strategic.sqlite'),
)

app.config.from_pyfile('config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/graphics/<path:path>')
def mouse_flowfield(path):
    return render_template('mouse-flowfield.html')

@app.route('/cooking')
def cooking():
    return render_template('strategy.html')

