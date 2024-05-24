#!/usr/bin/env python3

from app import db, bcrypt


class User(db.Model):
    # Define the columns for the user table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def set_password(self, password):
        """Generate a hashed password and store it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if the pasword matches the stored hashed password"""
        return bcrypt.check_password_hash(self.password, password)
