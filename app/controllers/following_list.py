#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: followers.py
# Author: Steve Tautonico
# Date Created: 5/3/2019
# Date Last Modified: 5/3/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Shows the list of followers"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template
from flask_login import login_required
from app.models import User

blueprint = Blueprint("following_list", __name__)


@blueprint.route("/followers/list/<username>")
@login_required
def following_list(username):
    # Create list to store followed users
    follow_list = []
    user = User.query.filter_by(username=username).first()
    if user.following:
        for follow in user.following.split(","):
            follow_list.append(User.query.filter_by(id=int(follow)).first())
    return render_template("followinglist.html", title="Following", follow_list=follow_list)