#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: __init__.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 5/03/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""The initialization file for the main 'app' package"""
# =============================================================================
# Imports
# =============================================================================
from flask import Flask, abort
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

__author__ = "Steve Tautonico"
__contact__ = "stautonico@gmail.com"
__date__ = "4/30/2019"

app = Flask(__name__)
app.config["SECRET_KEY"] = '96832c3f32b9a586095cf19384a9cccd1d51c9683f6e2239979d258cb975ba4f'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LcaaZkUAAAAAAX5Ff8gbbKglzAvHl31A7pbVYbM"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LcaaZkUAAAAADUqadT2yzMA0mHD_m0h48D_aVMg"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'
login_manager.login_message_category = "info"

from . import controllers
from .models import User


def register_blueprints(app):
    """Register blueprints."""
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.credits.blueprint)
    app.register_blueprint(controllers.login.blueprint)
    app.register_blueprint(controllers.account.blueprint)
    app.register_blueprint(controllers.update_account.blueprint)
    app.register_blueprint(controllers.logout.blueprint)
    app.register_blueprint(controllers.new_post.blueprint)
    app.register_blueprint(controllers.post.blueprint)
    app.register_blueprint(controllers.feed.blueprint)
    app.register_blueprint(controllers.edit_post.blueprint)
    app.register_blueprint(controllers.delete_post.blueprint)
    app.register_blueprint(controllers.following.blueprint_follow)
    app.register_blueprint(controllers.following.blueprint_unfollow)
    app.register_blueprint(controllers.search_account.blueprint)
    app.register_blueprint(controllers.following_list.blueprint)


register_blueprints(app)


def get_user_post(post):
    author = User.query.filter_by(id=post.user_id).first()
    return author


def get_user_from_id(id):
    user = User.query.filter_by(id=id).first()
    return user


app.jinja_env.globals.update(get_user_post=get_user_post)
app.jinja_env.globals.update(get_user_from_id=get_user_from_id)


# @app.errorhandler(Exception)
# def handle_error(e):
#     code = 500
#     if isinstance(e, HTTPException):
#         code = e.code
#     return render_template("error.html", code=str(code)), code


@app.route("/error/<errorcode>", methods=["GET", "POST"])
def force_code(errorcode):
    abort(int(errorcode))
