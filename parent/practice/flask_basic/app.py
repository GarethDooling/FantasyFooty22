from flask import Flask 

app = Flask(__name__)

@app.route('/')
def welcome_ff22():
    return "Welcome FF22!"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
    