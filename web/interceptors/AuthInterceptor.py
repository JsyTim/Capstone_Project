# -*- coding: utf-8 -*-
from application import app
from flask import request, g, redirect

from common.models.admin.Admin import Admin
from common.libs.admin.AdminService import (AdminService)
from common.libs.UrlManager import (UrlManager)
# from common.libs.LogService import LogService
import re


# check before every request
@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    # 如果是静态文件, 不查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    if '/mini' in path:
        return

    admin_info = check_login()
    # set global admin username
    g.current_admin = None
    if admin_info:
        g.current_admin = admin_info

    #加入日志
    # LogService.addAccessLog()

    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return

    if not admin_info:
        return redirect(UrlManager.buildUrl("/admin/login"))

    return


'''
判断用户是否已经登录
'''


def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None

    if '/mini' in request.path:
        app.logger.info(request.path)
        auth_cookie = request.headers.get("Authorization")
        app.logger.info(request.headers.get("Authorization"))


    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        admin_info = Admin.query.filter_by(aid=auth_info[1]).first()
    except Exception:
        return False

    # chech data is empty or not
    if admin_info is None:
        return False

    #  vertify cookie
    if auth_info[0] != AdminService.geneAuthCode(admin_info):
        return False

    if admin_info.status != 1:
        return False

    return admin_info