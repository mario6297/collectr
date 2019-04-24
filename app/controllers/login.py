# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user

from app.forms import LogInForm
from app import bcrypt
from app.models import User

blueprint = Blueprint("login", __name__)


@blueprint.route('/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_user.home_user', username=current_user.username))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('home_user.home_user', username=current_user.username))
        else:
            flash("Login Unsuccessful. Please Check Email and Password", "danger")
    return render_template("login.html", form=form)
