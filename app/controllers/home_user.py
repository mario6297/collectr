from flask import Blueprint, render_template
from flask_login import current_user, login_required

blueprint = Blueprint("home_user", __name__)


@blueprint.route("/home/logged_in")
@login_required
def home_user():
    return render_template("home_user.html", title="Home")