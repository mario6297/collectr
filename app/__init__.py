from flask import Flask, abort
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = '96832c3f32b9a586095cf19384a9cccd1d51c9683f6e2239979d258cb975ba4f'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LcaaZkUAAAAAAX5Ff8gbbKglzAvHl31A7pbVYbM"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LcaaZkUAAAAADUqadT2yzMA0mHD_m0h48D_aVMg"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'
login_manager.login_message_category = "info"

from . import controllers


def register_blueprints(app):
    """Register blueprints."""
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.credits.blueprint)
    app.register_blueprint(controllers.login.blueprint)
    app.register_blueprint(controllers.home_user.blueprint)
    app.register_blueprint(controllers.update_account.blueprint)
    app.register_blueprint(controllers.logout.blueprint)


register_blueprints(app)


# @app.errorhandler(Exception)
# def handle_error(e):
#     code = 500
#     if isinstance(e, HTTPException):
#         code = e.code
#     return render_template("error.html", code=str(code)), code


@app.route("/error/<errorcode>", methods=["GET", "POST"])
def force_code(errorcode):
    abort(int(errorcode))
