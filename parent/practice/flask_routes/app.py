from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home/<int:number>')
def number_example(number):
    answer =  number * number 
    return str(answer)

@app.route('/about')
def about():
    return 'This is the about page for FF22'

@app.route('/signup')
def signup():
    return 'This is the sign up page for FF22'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)