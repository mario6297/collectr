# -*- coding: utf-8 -*-
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
