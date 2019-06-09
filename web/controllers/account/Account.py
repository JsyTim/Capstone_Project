# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, jsonify
from common.libs.Helper import ops_render, iPagination, getCurrentDate
from common.models.admin.Admin import Admin
from application import app, db
from common.libs.UrlManager import UrlManager
from common.libs.admin.AdminService import AdminService
# from common.libs.LogService import LogService
from common.models.log.App_access_log import AppAccessLog
from sqlalchemy import or_
route_account = Blueprint('account_page', __name__)


@route_account.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Admin.query

    if 'mix_kw' in req:
        rule = or_(Admin.nickname.ilike("%{0}%".format(req['mix_kw'])), Admin.mobile.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)

    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Admin.status == int(req['status']))

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    limit = app.config['PAGE_SIZE'] * page
    list = query.order_by(Admin.aid).all()[offset: limit]
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    return ops_render("account/index.html", resp_data)


@route_account.route("/info")
def info():
    resp_data = {}
    # get 方法用args
    req = request.args
    # get 方法需要默认值
    aid = int(req.get('id', 0))
    reback_url = UrlManager.buildUrl("/account/index")
    if aid < 1:
        return redirect(reback_url)

    info = Admin.query.filter_by(aid=aid).first()
    if not info:
        return redirect(reback_url)

    access_list = AppAccessLog.query.filter_by(aid=aid).order_by(AppAccessLog.id.desc()).limit(10).all()
    resp_data['info'] = info
    resp_data['access_list'] = access_list
    return ops_render("account/info.html", resp_data)


@route_account.route("/set", methods=["GET", "POST"])
def set():
    # default_pwd = "******"
    if request.method == "GET":
        resp_data = {}
        req = request.args
        aid = int(req.get("id", 0))
        info = None
        if aid:
            info = Admin.query.filter_by(aid=aid).first()
        resp_data['info'] = info
        return ops_render("account/set.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    email = req['email'] if 'email' in req else ''
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名"
        return jsonify(resp)

    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的手机号码"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱"
        return jsonify(resp)

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的登录用户名"
        return jsonify(resp)

    if login_pwd is None or len(email) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的登录密码"
        return jsonify(resp)

    has_in = Admin.query.filter(Admin.login_name == login_name, Admin.aid != id).first()
    if has_in:
        resp['code'] = -1
        resp['msg'] = "该登录名已存在，请换一个试试"
        return jsonify(resp)

    admin_info = Admin.query.filter_by(aid=id).first()
    if admin_info:
        model_admin = admin_info
    else:
        model_admin = Admin()
        model_admin.created_time = getCurrentDate()
        model_admin.login_salt = AdminService.geneSalt()

    model_admin.nickname = nickname
    model_admin.mobile = mobile
    model_admin.email = email
    model_admin.login_name = login_name
    # if login_pwd != default_pwd:
    #     if admin_info and admin_info.aid == 1:
    #         resp['code'] = -1
    #         resp['msg'] = "该用户是演示账号，不准修改密码和登录用户名"
    #         return jsonify(resp)

        # model_admin.login_pwd = AdminService.genePwd(login_pwd, model_admin.login_salt)

    model_admin.updated_time = getCurrentDate()
    db.session.add(model_admin)
    db.session.commit()
    return jsonify(resp)


@route_account.route("/ops", methods=["POST"])
def ops():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号"
        return jsonify(resp)

    if act not in ['remove', 'recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试"
        return jsonify(resp)

    admin_info = Admin.query.filter_by(aid=id).first()
    if not admin_info:
        resp['code'] = -1
        resp['msg'] = "指定账号不存在"
        return jsonify(resp)

    if act == "remove":
        admin_info.status = 0
    elif act == "recover":
        admin_info.status = 1

    if admin_info and admin_info.aid == 1:
        resp['code'] = -1
        resp['msg'] = "该用户是演示账号，不准操作账号"
        return jsonify(resp)

    admin_info.update_time = getCurrentDate()
    db.session.add(admin_info)
    db.session.commit()
    return jsonify(resp)
