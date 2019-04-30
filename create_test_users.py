#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: create_test_users.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Creates filler 'test' and adds it to the database"""
# =============================================================================
# Imports
# =============================================================================

from app import db
from app.models import User

print("[INFO] Creating new users...")
test1 = User(first_name="Test", last_name="User1", username="Test_User_1".lower(), email="test1@gmail.com", password='lockedsecurepasswordfortestuser')

test2 = User(first_name="Test", last_name="User2", username="Test_User_2".lower(), email="test2@gmail.com", password='lockedsecurepasswordfortestuser')

test3 = User(first_name="Test", last_name="User3", username="Test_User_3".lower(), email="test3@gmail.com", password='lockedsecurepasswordfortestuser')

test4 = User(first_name="Test", last_name="User4", username="Test_User_4".lower(), email="test4@gmail.com", password='lockedsecurepasswordfortestuser')

test5 = User(first_name="Test", last_name="User5", username="Test_User_5".lower(), email="test5@gmail.com", password='lockedsecurepasswordfortestuser')

print("[INFO] Adding users to database...")
db.session.add(test1)
db.session.add(test2)
db.session.add(test3)
db.session.add(test4)
db.session.add(test5)
db.session.commit()

print("[+] Successfully added 5 test users!")