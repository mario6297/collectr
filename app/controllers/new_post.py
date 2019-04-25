from flask import render_template, Blueprint
from flask_login import login_required

from app.forms import NewPost

blueprint = Blueprint("new_post", __name__)


@blueprint.route("/newpost/", methods=["GET", "POST"])
@login_required
def new_post():
    form = NewPost()
    return render_template("new_post.html", title="New Post", form=form)
