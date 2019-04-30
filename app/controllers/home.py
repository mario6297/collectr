#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: home.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles the forms and registration for users on the home page"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import current_user

from app.forms import RegForm

from app.services.user_management import register

blueprint = Blueprint('home', __name__)


@blueprint.route('/', methods=["POST", "GET"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed', username=current_user.username))
    form = RegForm()
    if form.validate_on_submit():
        result = register(form)
        if result:
            flash("Account successfully created!", "success")
            return redirect(url_for("login.login"))
        else:
            abort(500)
    return render_template('index.html', form=form)
