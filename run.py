#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: run.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""The script that executes the webapp"""
# =============================================================================
# Imports
# =============================================================================
import logging
from datetime import datetime
from config import config

from app import app
from config import config

if __name__ == "__main__":
    if config["logger"]:
        logging.basicConfig(filename='./logs/{}.log'.format(datetime.now().strftime("%Y-%m-%d %H-%M")), level=logging.DEBUG)
    app.run(config["ip"], threaded=True, debug=True, port=5000)
