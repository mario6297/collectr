from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Post

blueprint = Blueprint("post", __name__)


@blueprint.route('/post/<id>')
@login_required
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template("post.html", post=post)
