from flask_wtf import FlaskForm, RecaptchaField
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
    recaptcha = RecaptchaField()

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
