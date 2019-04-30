#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: new_post.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles forms and logic for creating new posts and adding it to the db"""
# =============================================================================
# Imports
# =============================================================================
from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.forms import NewPost
from app.models import Post
from app.services.image import save_post

blueprint = Blueprint("new_post", __name__)


@blueprint.route("/newpost/", methods=["GET", "POST"])
@login_required
def new_post():
    form = NewPost()
    if form.validate_on_submit():
        image_filename = save_post(form.picture.data)
        post = Post(title=form.title.data, image=image_filename, description=form.description.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.post', id=post.id))
    return render_template("new_post.html", title="New Post", form=form)
