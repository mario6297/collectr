#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: image.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 4/30/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""Module handles saving images from forms and re-scaling to fit and save space"""
# =============================================================================
# Imports
# =============================================================================
import os
from datetime import datetime

from PIL import Image, ImageSequence
from flask_login import current_user

from app import app


def save_pfp(picture):
    file_ext = picture.filename.split(".")
    picture_filename = current_user.username + "." + file_ext[1]
    pic_path = os.path.join(app.root_path, "static/pfp", picture_filename)

    image_size = (300, 300)
    i = Image.open(picture)
    i = i.resize(image_size)

    i.save(pic_path)
    return picture_filename


def save_post(picture):
    file_ext = picture.filename.split(".")
    picture_filename = current_user.username + "_" + datetime.utcnow().strftime("%H%M%S%m%d%Y") + "." + file_ext[1]
    pic_path = os.path.join(app.root_path, "static/posts", picture_filename)

    i = Image.open(picture)

    width, height = i.size
    if width > 1080 or height > 1080:
        biggest = max(width, height)
        scale = (1080/biggest)
        print(scale)
        final_size = (round(width*scale), round(height*scale))
        i = i.resize(final_size)

    i.save(pic_path)
    return picture_filename

