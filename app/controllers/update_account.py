import os
from PIL import Image

from flask import Blueprint, flash, request, render_template, redirect, url_for
from flask_login import current_user, login_required

from app import db, app
from app.forms import UpdateAccount

blueprint = Blueprint("update_account", __name__)


def save_picture(picture):
    file_ext = picture.filename.split(".")
    picture_filename = current_user.username + "." + file_ext[1]
    pic_path = os.path.join(app.root_path, "static/pfp", picture_filename)

    image_size = (300, 300)
    i = Image.open(picture)
    i = i.resize(image_size)

    i.save(pic_path)
    return picture_filename


@blueprint.route("/update_account/", methods=["GET", "POST"])
@login_required
def update_account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_filename = save_picture(form.profile_picture.data)
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
