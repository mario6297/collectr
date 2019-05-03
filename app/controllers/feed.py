#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: feed.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 5/3/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles the users feed containing posts from followed users"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import User, Post

blueprint = Blueprint("feed", __name__)


@blueprint.route('/feed/')
@login_required
def feed():
    following = []
    # The un-flattened posts list
    sub_posts = []
    # List for flattened posts
    posts = []
    for usr_following in current_user.following.split(","):
        user = User.query.filter_by(id=int(usr_following)).first()
        following.append(user)
        sub_posts.append(Post.query.filter_by(user_id=user.id).all())

    for sublist in sub_posts:
        for item in sublist:
            posts.append(item)
    posts.sort(key=lambda x: x.date_posted, reverse=True)
    return render_template("feed.html", title="Feed", following=following, posts=posts)
