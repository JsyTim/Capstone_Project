# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = 'BOOK'


##过滤url
IGNORE_URLS = [
    "^/admin/login"

]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

MINI_IGNORE_URLS = [
    "^/mini"
]

APP = {
    'domain': 'http://192.168.56.1:8999'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

MINA_APP = {
    'appid': 'wx26658096642fb61a',
    'appkey': 'b5e3a4aa9e061aeef3efc0b9975f75fe',
    # 'paykey': 'xxxxxxxxxxxxxx换自己的',
    # 'mch_id': 'xxxxxxxxxxxx换自己的',
    'callback_url': '/api/order/callback'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}


PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
