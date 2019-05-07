#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: discover.py
# Author: Steve Tautonico
# Date Created: 5/5/2019
# Date Last Modified: 5/5/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles the discover feed page"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Post

blueprint = Blueprint('discover', __name__)


@blueprint.route('/discover/')
@login_required
def discover():
    featured_posts = Post.query.filter_by(featured=True).all()
    print(featured_posts)

    return render_template("discover.html", title="Discover", posts=featured_posts)
