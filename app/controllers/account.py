#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: account.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Account page for a user. Preforms several checks and passes data to the HTML"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, url_for, abort
from flask_login import login_required
from app.models import User


blueprint = Blueprint("account", __name__)


@blueprint.route("/account/<username>")
@login_required
def account(username):
    if not username:
        abort(404)
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    image = url_for('static', filename='pfp/' + user.image_file)
    return render_template("account.html", title="Home", image=image, user=user)
