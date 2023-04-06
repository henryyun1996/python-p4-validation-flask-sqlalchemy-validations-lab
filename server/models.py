from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    phone_number = db.Column(db.Integer,
                            db.CheckConstraint('LENGTH(phone_number) = 10'),
                            nullable=False)

    def __repr__(self):
        return f'<Author: {self.name} | Phone Number: {self.phone_number}>'
    
    @validates('name')
    def validate_name(self, key, name):
        if name == '':
            raise ValueError("You must enter a name.")
        return name

    @validates('phone_number')
    def validates_phone_number_length(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must be 10 digits.")
        return phone_number

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String,
                        db.CheckConstraint('LENGTH(content) >= 250'),
                        nullable=False)
    summary = db.Column(db.String,
                        db.CheckConstraint('LENGTH(summary) < 250'),
                        nullable=False)
    category = db.Column(db.String)

    @validates('category')
    def validate_category(self, key, category):
        if category != 'Fiction' and category != 'Non-fiction':
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return category
    
    @validates('title')
    def title_is_clickbait(self, key, title):
        click_bait_words = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(word in title for word in click_bait_words):
            raise ValueError("Title is not clickbait-y enough.")
        return title