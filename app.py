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

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    return "The student has passed successfully with score: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The student has failed due to score: " + str(score)

if __name__=='__main__':
    app.run(debug=True)
