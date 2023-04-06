from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    phone_number = db.Column(db.Integer,
                            db.CheckConstraint('len(phone_number) = 10'),
                            nullable=False)

    def __repr__(self):
        return f'<Author: {self.name} | Phone Number: {self.phone_number}>'
    
    @validates('name')
    def validate_name(self, key, name):
        if name == '':
            raise ValueError("You must enter a name.")
        return name

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String,
                        db.CheckConstraint('len(content) >= 250'),
                        nullable=False)
    summary = db.Column(db.String,
                        db.CheckConstraint('len(summary) < 250'),
                        nullable=False)
    category = db.Column(db.String)

    @validates('category')
    def validate_category(self, key, category):
        if category != 'Fiction' and category != 'Non-fiction':
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return category