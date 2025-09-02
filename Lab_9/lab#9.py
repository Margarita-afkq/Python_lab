from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Visited cities')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(300))
    visit_date = db.Column(db.String(100))

    def __repr__(self):
        return f'City{self.id}. {self.town} - {self.visit_date}'

@app.route('/')
def main():
    cities = City.query.all()
    return render_template('index.html', cities_list=cities)

@app.route('/add', methods=['POST'])
def add_city():
    data = request.json
    city = City(**data)
    db.session.add(city)
    db.session.commit()
    return 'OK'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
