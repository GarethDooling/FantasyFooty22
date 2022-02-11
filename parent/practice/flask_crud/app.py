
from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    founded = db.Column(db.Integer, nullable=False)
    players = db.relationship('Player', backref='team')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    
if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')

    

