from flask import render_template, flash
from app import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from . import controllers

"""Main Routes"""
# @app.route("/")
# def home():
#     return render_template("index.html")
#
#
# @app.route("/credits")
# def credits():
#     return render_template("credits.html")


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.credits.blueprint)
    print(app)
    return None

def register_errorhandlers(app):
    # """Register error handlers."""
    # @app.errorhandler(401)
    # def internal_error(error):
    #     return render_template('401.html'), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    # @app.errorhandler(500)
    # def internal_error(error):
    #     return render_template('500.html'), 500

    return None