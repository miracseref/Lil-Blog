from . import db
from .models import User
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        # Min 8 characters: {8,}
        # At least one uppercase: (?=.*?[A-Z])
        # At least one lowercase: (?=.*?[a-z])
        # At least one digit: (?=.*?[0-9])
        # At least one special character: (?=.*?[#?!@$%^&*-])
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

        email_pattern = "^[a-z]+[-_$.a-z]*@[a-z]*\.[a-z]+$"

        if email_exists:
            flash('This email is already in use.', category='error')
        elif username_exists:
            flash('This username is already in use.', category='error')
        elif password != confirmation:
            flash('The password don\'t match!', category='error')
        elif len(username) < 2:
            flash('The username is too short.', category='error')
        elif not re.match(password_pattern, password):
            flash('The password is not strong enough.', category='error')
        elif not re.match(email_pattern, email, re.IGNORECASE):
            flash("This email is invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
