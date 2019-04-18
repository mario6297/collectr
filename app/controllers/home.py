# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from app.forms import RegForm
from app import db, bcrypt
from app.models import User

blueprint = Blueprint('home', __name__)


@blueprint.route('/', methods=["POST", "GET"])
def home():
    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("credits.credits"))
    return render_template('index.html', form=form)
