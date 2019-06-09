from flask import Blueprint, request, jsonify, make_response, redirect, g
from common.libs.admin.AdminService import (AdminService)
from application import app, db
from common.libs.UrlManager import (UrlManager)
from common.libs.Helper import (ops_render)
from common.models.admin.Admin import Admin
import json

route_admin = Blueprint('admin_page', __name__)


@route_admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return ops_render("admin/login.html")

    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录密码"
        return jsonify(resp)

    #  login is unique key, so just need to pick up the first
    admin_info = Admin.query.filter_by(login_name=login_name).first()
    if not admin_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码"
        return jsonify(resp)

    if admin_info.login_pwd != AdminService.genePwd(login_pwd, admin_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码"
        return jsonify(resp)

    if admin_info.status != 1:
        resp['code'] = -1
        resp['msg'] = "账号已被禁用，请联系管理员处理"
        return jsonify(resp)

    # set cookies
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功'}))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        AdminService.geneAuthCode(admin_info), admin_info.aid), 60 * 60 * 24 * 30)  # 保存30天
    return response


@route_admin.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        return ops_render("admin/edit.html", {'current': 'edit'})

    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    email = req['email'] if 'email' in req else ''

    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名"
        return jsonify(resp)

    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的手机号"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱"
        return jsonify(resp)

    admin_info = g.current_admin
    admin_info.nickname = nickname
    admin_info.mobile = mobile
    admin_info.email = email

    db.session.add(admin_info)
    db.session.commit()
    return jsonify(resp)


@route_admin.route("/reset-pwd", methods=["GET", "POST"])
def resetPwd():
    if request.method == "GET":
        return ops_render("admin/reset_pwd.html", {'current': 'reset-pwd'})

    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    old_password = req['old_password'] if 'old_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else ''

    if old_password is None or len(old_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的原密码"
        return jsonify(resp)

    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码"
        return jsonify(resp)

    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = "请重新输入，新密码和原密码不能相同"
        return jsonify(resp)

    admin_info = g.current_admin

    if admin_info.aid == 1:
        resp['code'] = -1
        resp['msg'] = "该用户是演示账号，不允许修改密码和登录用户名"
        return jsonify(resp)

    admin_info.login_pwd = AdminService.genePwd(new_password, admin_info.login_salt)

    db.session.add(admin_info)
    db.session.commit()

    # 设置cookies
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        AdminService.geneAuthCode(admin_info), admin_info.aid), 60 * 60 * 24 * 30)  # 保存30天
    return response


@route_admin.route("/logout")
def logout():
    '''
    清除cookies，回到login界面
    :return: response
    '''
    response = make_response(redirect(UrlManager.buildUrl("/admin/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response