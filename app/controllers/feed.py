#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: feed.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles the users feed containing posts from followed users"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import User

blueprint = Blueprint("feed", __name__)


@blueprint.route('/feed/')
@login_required
def feed():
    f_un = []
    try:
        following = current_user.following.split(',')
        for follow in following:
            f_un.append(User.query.filter_by(id=follow).first().username)
    except:
        pass
    return render_template("feed.html", title="Feed", following=f_un)
