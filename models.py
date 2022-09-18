from datetime import datetime
from database import db


class User(db.Model):
    __tablename__ = "tbl_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def json(self):
        return {"id": self.id, "username": self.username, "password": self.password}

    @classmethod
    def get_item_by_name(cls, username, password):
        return cls.query.filter_by(username=username, password=password).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Category(db.Model):
    __tablename__ = "tbl_category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Category %r>" % self.name

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def get_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Transaction(db.Model):
    __tablename__ = "tbl_transaction"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("tbl_user.id"), nullable=False)

    user = db.relationship("User", backref=db.backref("transactions", lazy=True))

    category_id = db.Column(
        db.Integer, db.ForeignKey("tbl_category.id"), nullable=False
    )

    category = db.relationship(
        "Category", backref=db.backref("transactions", lazy=True)
    )

    def __repr__(self):
        return "<Transaction %r>" % self.name

    def __init__(self, name, description, date, user_id, category_id):
        self.name = name
        self.description = description
        self.date = date
        self.user_id = user_id
        self.category_id = category_id

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "user": self.user.json(),
            "category": self.category.json(),
        }

    @classmethod
    def get_item_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_item_by_name(cls, name):
        return cls.query.filter_by(id=name)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
