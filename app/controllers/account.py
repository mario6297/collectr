#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: account.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 5/02/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Account page for a user. Preforms several checks and passes data to the HTML"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, url_for, abort
from flask_login import login_required, current_user

from app.models import User, Post

blueprint = Blueprint("account", __name__)


@blueprint.route("/account/<username>")
@login_required
def account(username):
    # Create a blank list to store the int versions of the following user ids
    current_user_following_int = []
    # Grab the current user's following list and split it by comma
    try:
        current_user_following_str = current_user.following.split(',')
        # Iterate through all the ids in the string list
        for following in current_user_following_str:
            # append the int version to the int ids list
            try:
                current_user_following_int.append(int(following))
            except ValueError:
                break
    except Exception:
        pass
    if not username:
        abort(404)
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    posts = Post.query.filter_by(user_id=user.id).all()
    image = url_for('static', filename='pfp/' + user.image_file)
    return render_template("account.html", title=user.username, image=image, user=user, posts=posts,
                           total_posts=len(posts),
                           current_user_following=current_user_following_int)
