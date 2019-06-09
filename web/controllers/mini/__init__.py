# -*- coding: utf-8 -*-
from flask import Blueprint
route_mini = Blueprint('mini_page', __name__)


from web.controllers.mini.Member import *
from web.controllers.mini.Book import *
from web.controllers.mini.Order import *
from web.controllers.mini.My import *
from web.controllers.mini.Cart import *
from web.controllers.mini.Address import *


@route_mini.route("/")
def index():
    return "昕悦二手书商城"