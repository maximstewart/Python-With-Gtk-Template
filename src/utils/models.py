# Python imports

# Lib imports
from flask_sqlalchemy import SQLAlchemy

# Apoplication imports


_db = SQLAlchemy()


class User(_db.Model):
    email       = _db.Column(_db.Text())
    username    = _db.Column(_db.Text())
    password    = _db.Column(_db.Text())
    id          = _db.Column(_db.Integer, primary_key=True,
                            unique=True, autoincrement=True)

    def __repr__(self):
        return f"'{self.email}', '{self.username}', '{self.password}', '{self.id}'"


_db.create_all()
