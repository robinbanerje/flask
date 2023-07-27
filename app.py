from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home page</h1>"

@app.route('/welcome')
def welcome():
    return "<button>Welcome to flask</button>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<score>')
def success(score):
    return "The student has passed successfully with score: " + score

@app.route('/fail/<score>')
def fail(score):
    return "The student has failed due to score: " + score

if __name__=='__main__':
    app.run(debug=True)
