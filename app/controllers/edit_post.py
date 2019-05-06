#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: edit_post.py
# Author: Steve Tautonico
# Date Created: 5/1/2019
# Date Last Modified: 5/1/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles editing posts"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, redirect, abort, flash, request, url_for
from flask_login import current_user, login_required

from app import db
from app.models import Post
from app.forms import EditPost

blueprint = Blueprint("edit_post", __name__)


@blueprint.route('/edit_post/<id>', methods=["GET", "POST"])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        abort(404)
    if post.user_id != current_user.id:
        flash("You can't edit someone else's post", "danger")
        return redirect(url_for("post.post", id=id))
    form = EditPost()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        db.session.commit()
        flash("Post edited successfully", "success")
        return redirect(url_for('post.post', id=id))
    elif request.method == "GET":
        form.title.data = post.title
        form.description.data = post.description
    return render_template("edit_post.html", title="Edit Post", form=form, post=post)