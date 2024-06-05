#!/usr/bin/env python3

from flask import render_template, url_for, flash, redirect, session
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User
import bcrypt


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            'Your account has been created! You are now able to log in',
            'success'
            )
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(
                'Login Unsuccessful. Please check email and password',
                'danger'
                )
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    session.clear()
    flash('You have been logged out!', 'success')
    return redirect(url_for('home'))
