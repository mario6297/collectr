# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('errors', __name__)


@blueprint.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
