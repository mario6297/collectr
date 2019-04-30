#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: reset_database.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Removed and recreates all tables in the SQLAlchemy Database. Also wipes all records"""
# =============================================================================
# Imports
# =============================================================================
from app import db

print("[INFO] Dropping Database Entries...")
db.drop_all()
print("[+] Successfully dropped!")

print("[INFO] Recreating Database Models...")
db.create_all()
print("[+] Successfully created!")

