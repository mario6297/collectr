#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: user_management.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Script to handle user accounts"""
# =============================================================================
# Imports
# =============================================================================
from app import bcrypt, db
from app.models import User


def register(form):
    try:
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data.lower(),
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return True
    except:
        return False

