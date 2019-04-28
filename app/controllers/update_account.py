from flask import Blueprint, flash, request, render_template, redirect, url_for
from flask_login import current_user, login_required

from app import db
from app.forms import UpdateAccount
from app.services.image import save_pfp

blueprint = Blueprint("update_account", __name__)


@blueprint.route("/update_account/", methods=["GET", "POST"])
@login_required
def update_account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_filename = save_pfp(form.profile_picture.data)
            current_user.image_file = picture_filename
        current_user.email = form.email.data
        current_user.username = form.username.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash("Your account has been updated", "success")
        return redirect(url_for('home.home'))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.location.data = current_user.location
        form.bio.data = current_user.bio

    return render_template("update_account.html", title="Update Account", form=form)
