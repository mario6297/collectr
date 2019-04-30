#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: credits.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Credits page displaying information about external resources used"""
# =============================================================================
# Imports
# =============================================================================
from flask import Blueprint, render_template

blueprint = Blueprint('credits', __name__)


@blueprint.route('/credits/')
def credits():
    return render_template('credits.html', title="Credits")
