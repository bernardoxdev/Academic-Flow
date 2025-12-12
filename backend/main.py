import os

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

UPLOAD_FOLDER = os.path.join('backend', 'libs', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Flask Site
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saber_mais')
def saber_mais():
    pass

@app.route('/entrar')
def entrar():
    pass

# Run
if __name__ == '__main__':
    app.run(debug=True)