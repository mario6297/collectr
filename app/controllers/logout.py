#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: logout.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Handles the log-out for users"""
# =============================================================================
# Imports
# =============================================================================
from flask import flash, url_for, redirect, Blueprint
from flask_login import logout_user, current_user

blueprint = Blueprint("logout", __name__)


@blueprint.route('/logout/')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logged out successfully!", "success")
        return redirect(url_for('home.home'))
    flash("No user is currently logged in", "warning")
    return redirect(url_for('home.home'))
