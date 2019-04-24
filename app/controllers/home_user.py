from flask import Blueprint, render_template, url_for, abort
from flask_login import login_required
from app.models import User


blueprint = Blueprint("home_user", __name__)


@blueprint.route("/account/<username>")
@login_required
def home_user(username):
    if not username:
        abort(404)
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    image = url_for('static', filename='pfp/' + user.image_file)
    return render_template("home_user.html", title="Home", image=image, user=user)
