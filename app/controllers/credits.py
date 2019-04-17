# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('credits', __name__)


@blueprint.route('/credits')
def credits():
    return render_template('credits.html')
