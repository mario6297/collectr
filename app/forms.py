#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Filename: forms.py
# Author: Steve Tautonico
# Date Created: 4/30/2019
# Date Last Modified: 5/04/2019
# Python Version: 3.6 - 3.7
# =============================================================================
"""The forms that accept inputs from the html"""
from flask_login import current_user
# =============================================================================
# Imports
# =============================================================================
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

import common_passwords
from app.models import User
from disposable_emails import emails


class RegForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo('password'), Length(min=4)])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register")
    # recaptcha = RecaptchaField()

    invalid_characters = ["\\", "/", ":", "*", "?", "<", ">", "|", '"', "'", ";", "%"]

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("A user with that username already exists.")
        for char in self.invalid_characters:
            if char in username.data:
                raise ValidationError(f"{char} is an invalid character.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already taken.")
        domain = email.data.split("@")
        try:
            if domain[1] in emails:
                raise ValidationError("Please don't use a disposable email address.")
        except Exception:
            raise ValidationError("Please use a valid email.")

    def validate_password(self, password):
        if password.data in common_passwords.passwords:
            raise ValidationError("Please use a safer password")


class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class UpdateAccount(FlaskForm):
    email = StringField("Email", validators=[Email()])
    username = StringField("Username", validators=[Length(max=20)])
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    location = StringField("Location", validators=[Length(max=50)])
    bio = StringField("Bio", validators=[Length(max=200)])
    profile_picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png", "gif"])])
    submit = SubmitField("Update")

    invalid_characters = ["\\", "/", ":", "*", "?", "<", ">", "|", '"', "'", ";", "%"]

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if username.data != current_user.username:
            if user:
                raise ValidationError("That username is already taken.")
            for char in self.invalid_characters:
                if char in username.data:
                    raise ValidationError(f"{char} is an invalid character.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if email.data != current_user.email:
            if user:
                raise ValidationError("That email is already taken.")
            domain = email.data.split("@")
            try:
                if domain[1] in emails:
                    raise ValidationError("Please don't use a disposable email address.")
            except Exception:
                raise ValidationError("Please use a valid email.")


class NewPost(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=60)])
    picture = FileField("Image", validators=[FileAllowed(["jpg", "png", "gif"]), DataRequired()])
    description = StringField("Description", validators=[Length(max=540)])
    submit = SubmitField("Post")


class EditPost(FlaskForm):
    title = StringField("Title", validators=[Length(min=3, max=60)])
    description = StringField("Description", validators=[Length(max=540)])
    submit = SubmitField("Edit")


class DeletePost(FlaskForm):
    submit = SubmitField("Delete")


class SearchAccount(FlaskForm):
    username = StringField("Username", validators=[Length(min=4)])
    submit = SubmitField("Search")
