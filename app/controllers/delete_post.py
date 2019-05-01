#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: delete_post.py
# Author: Steve Tautonico
# Date Created: 5/1/2019
# Date Last Modified: 5/1/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles confirmation of post deletion"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, abort, flash, url_for, redirect
from flask_login import current_user

from app import db
from app.forms import DeletePost
from app.models import Post

blueprint = Blueprint("delete_post", __name__)


@blueprint.route('/delete_post/<id>', methods=["POST", "GET"])
def delete_post(id):
    form = DeletePost()
    post = Post.query.filter_by(id=id).first()
    if not post:
        abort(404)
    if post.user_id != current_user.id:
        flash("You can't delete someone else's post", "danger")
        return redirect(url_for("post.post", id=id))
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted successfully", "success")
        return redirect(url_for('account.account', username=current_user.username))
    return render_template("delete_post.html", title="Delete Post", form=form)
