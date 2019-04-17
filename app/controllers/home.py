# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from app.forms import RegForm

blueprint = Blueprint('home', __name__)


@blueprint.route('/', methods=["POST", "GET"])
def home():
    form = RegForm()
    return render_template('index.html', form=form)
