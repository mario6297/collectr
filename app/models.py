#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: models.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""The tables and 'models' for the SQLAlchemy Database"""
# =============================================================================
# Imports
# =============================================================================
from datetime import datetime

from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), unique=False, nullable=False)
    last_name = db.Column(db.String(), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    password = db.Column(db.String(60), nullable=False)
    user_type = db.Column(db.String(), nullable=False, default="User")
    location = db.Column(db.String(), nullable=True)
    joined = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    bio = db.Column(db.String(200), nullable=True, unique=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    following = db.Column(db.String(), nullable=True)
    verified = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f"User('{self.username}', {self.email}, {self.id})"


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    featured = db.Column(db.Boolean(), nullable=False, default=False)
