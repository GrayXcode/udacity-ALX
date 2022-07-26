from dbus import MissingReplyHandlerException
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udacitystudio:falcon568@localhost:5432/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    citizen = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f'<User name={self.name}, age={self.age}>'


@app.route('/')
def index():
    return 'Successfully initiated'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
