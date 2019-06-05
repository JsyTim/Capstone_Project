from flask import Blueprint, request, jsonify, make_response, redirect, g
from common.libs.admin.AdminService import (AdminService)
from application import app, db
from common.libs.UrlManager import (UrlManager)
from common.libs.Helper import (ops_render)
from common.models.admin.Admin import Admin

route_admin = Blueprint('admin_page', __name__)


@route_admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return ops_render("admin/login.html")

    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    req = request.values
    # login_name = req['login_name'] if 'login_name' in req else ''
    # login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    #
    # if login_name is None or len(login_name) < 1:
    #     resp['code'] = -1
    #     resp['msg'] = "请输入正确的登录用户名"
    #     return jsonify(resp)
    #
    # if login_pwd is None or len(login_pwd) < 1:
    #     resp['code'] = -1
    #     resp['msg'] = "请输入正确的登录密码"
    #     return jsonify(resp)
    #
    # user_info = User.query.filter_by(login_name=login_name).first()
    # if not user_info:
    #     resp['code'] = -1
    #     resp['msg'] = "请输入正确的登录用户名和密码"
    #     return jsonify(resp)
    #
    # if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
    #     resp['code'] = -1
    #     resp['msg'] = "请输入正确的登录用户名和密码"
    #     return jsonify(resp)
    #
    # if user_info.status != 1:
    #     resp['code'] = -1
    #     resp['msg'] = "账号已被禁用，请联系管理员处理~~"
    #     return jsonify(resp)
    #
    # response = make_response(json.dumps({'code': 200, 'msg': '登录成功'}))
    # response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
    #     UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
    return resp
