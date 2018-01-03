import datetime

from server import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    email_confirmed = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, password, email):
        self.password = password
        self.email = email
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        """Add user to database"""
        db.session.add(self)
        db.session.commit()

    def tojson(self):
        """Represent user data as JSON object"""
        return {
            'email': self.email
        }
