from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Exoplanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(64), index=True)
    dist_from_earth = db.Column(db.Integer, index=True)
    planet_mass = db.Column(db.String(256))
    stellar_magnitude = db.Column(db.Float)
    discovery_date = db.Column(db.Integer, index=True)
    
db.create_all()


@app.route('/')
def index():
    exoplanets = Exoplanets.query
    return render_template('table.html', title='EXO',
                           exoplanets=exoplanets)


if __name__ == '__main__':
    app.run(debug=True)