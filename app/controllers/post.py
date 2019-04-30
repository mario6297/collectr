#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: post.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles display post and related information as well as redirects to related info"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Post, User

blueprint = Blueprint("post", __name__)


@blueprint.route('/post/<id>')
@login_required
def post(id):
    post = Post.query.filter_by(id=id).first()
    author = User.query.filter_by(id=post.user_id).first()
    date = post.date_posted.strftime("%B %d, %Y")
    return render_template("post.html", post=post, author=author, posted=date)
