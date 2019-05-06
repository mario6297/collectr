#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: following.py
# Author: Steve Tautonico
# Date Created: 5/2/2019
# Date Last Modified: 5/04/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Controls following and un-following of users"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, redirect, url_for, flash, abort, request
from flask_login import current_user, login_required

from app import db
from app.models import User

blueprint_follow = Blueprint("follow", __name__)
blueprint_unfollow = Blueprint("unfollow", __name__)


def add_user_to_follow_split(user):
    # Convert following to list
    user_following = current_user.following.split(",")
    # Add the new ID to the list
    user_following.append(str(user.id))
    # Remove the blank users
    if "" in user_following:
        user_following.remove("")
    current_user.following = ",".join(user_following)
    # Commit the changes
    db.session.commit()
    return redirect(url_for("account.account", username=user.username))


def add_user_to_follow(user):
    current_user.following = user.id
    db.session.commit()
    return redirect(url_for("account.account", username=user.username))


@blueprint_follow.route("/follow/<id>")
@login_required
def follow(id):
    # Find the user's record
    user = User.query.filter_by(id=id).first()
    # Check if the user doesn't exist
    if not user:
        abort(404)
    # Check if the user is the current user
    if user == current_user:
        flash("You cannot follow yourself", "warning")
        return redirect(request.referrer)
    # Check if the user isn't in the list of following
    try:
        if str(id) not in current_user.following.split(','):
            add_user_to_follow_split(user)
            return redirect(request.referrer)
        # If the user is on the following list
        else:
            flash("You are already following this user", "warning")
            return redirect(request.referrer)
    except Exception as e:
        try:
            if not current_user.following:
                add_user_to_follow(user)
                return redirect(request.referrer)
        except Exception:
            abort(500)


@blueprint_unfollow.route("/unfollow/<id>")
@login_required
def unfollow(id):
    # Find the user's record
    user = User.query.filter_by(id=id).first()
    # Check if the user doesn't exist
    if not user:
        abort(404)
    # Check if the user is the current user
    if user == current_user:
        flash("You cannot follow yourself", "warning")
    # Check if the user isn't in the list of following
    if str(id) in current_user.following.split(','):
        # Convert following to list
        user_following = current_user.following.split(",")
        # Add the new ID to the list
        user_following.remove(id)
        # Check if the user has 0 following
        if not user_following:
            current_user.following = None
        else:
            # Combine the list with commas and replace the users following
            current_user.following = ",".join(user_following)
        # Commit the changes
        db.session.commit()
        return redirect(url_for("account.account", username=user.username))
    # If the user is on the following list
    else:
        flash("You are not following this user", "warning")
        return redirect(request.referrer)
