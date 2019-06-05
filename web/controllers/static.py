# -*- coding: utf-8 -*-
from flask import Blueprint, send_from_directory
from application import app
route_static = Blueprint('static', __name__)


# for redirect static root path
@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)