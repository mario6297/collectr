#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: search_account.py
# Author: Steve Tautonico
# Date Created: 5/3/2019
# Date Last Modified: 5/3/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles searching of profiles and accounts"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from app.forms import SearchAccount
from app.models import User

blueprint = Blueprint("search_account", __name__)


@blueprint.route("/search-account/", methods=["GET", "POST"])
@blueprint.route("/search-account/<username>", methods=["GET", "POST"])
@login_required
def search_account(username=None):
    form = SearchAccount()
    if form.validate_on_submit():
        # Redirect to this same route but with an argument
        return redirect(url_for('search_account.search_account', username=form.username.data))
    # Check if there is the username argument
    if username:
        # Render the results page
        users = User.query.filter(User.username.like("%{}%".format(username))).all()
        if not users:
            flash("No users found!", "danger")
            return redirect(url_for('search_account.search_account'))
        else:
            return render_template("search_results.html", title="Results", users=users)
    # Otherwise, render the page with the form
    return render_template("search_account.html", title="Search", form=form)
