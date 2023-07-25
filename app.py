from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home page</h1>"

@app.route('/welcome')
def welcome():
    return "<h2>Welcome to flask</h2>"

@app.route('/index')
def index():
    return "<button>Welcome to index page</button>"

if __name__=='__main__':
    app.run(debug=True)