# -*- coding: utf-8 -*-
from web.controllers.mini import route_mini
from flask import request, jsonify, g
from application import app, db
from common.libs.UrlManager import UrlManager
from common.libs.Helper import getCurrentDate
from common.models.member.MemberAddress import MemberAddress


@route_mini.route("/address/index")
def AddressList():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    member_info = g.member_info
    list = MemberAddress.query.filter_by(status=1, member_id=member_info.id)\
        .order_by(MemberAddress.id.desc()).all()
    data_list = []
    if list:
        for item in list:
            tmp_data = {
                "id": item.id,
                "nickname": item.nickname,
                "mobile": item.mobile,
                "is_default": item.is_default,
                "address": "%s %s %s %s"%(item.province_str, item.city_str, item.dist_str, item.address),
            }
            data_list.append(tmp_data)
    resp['data']['list'] = data_list
    return jsonify(resp)


@route_mini.route("/address/set", methods=["POST"])
def AddressSet():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    nickname = req['nickname'] if 'nickname' in req else ''
    address = req['address'] if 'address' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''

    province_id = int(req['province_id']) if ('province_id' in req and req['province_id']) else 0
    province_str = req['province_str'] if 'province_str' in req else ''
    city_id = int(req['city_id']) if ('city_id' in req and req['city_id'])else 0
    city_str = req['city_str'] if 'city_str' in req else ''
    district_id = int(req['district_id']) if ('district_id' in req and req['district_id']) else 0
    district_str = req['district_str'] if 'district_str' in req else ''

    member_info = g.member_info

    if not nickname:
        resp['code'] = -1
        resp['msg'] = "请填写联系人姓名~~"
        return jsonify(resp)

    if not mobile:
        resp['code'] = -1
        resp['msg'] = "请填写手机号码~~"
        return jsonify(resp)

    if province_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择地区~~"
        return jsonify(resp)

    if city_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择地区~~"
        return jsonify(resp)

    if district_id < 1:
        district_str = ''

    if not address:
        resp['code'] = -1
        resp['msg'] = "请填写详细地址~~"
        return jsonify(resp)

    if not member_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    address_info = MemberAddress.query.filter_by(id=id, member_id=member_info.id).first()
    if address_info:
        model_address = address_info
    else:
        default_address_count = MemberAddress.query.filter_by(is_default=1, member_id=member_info.id, status=1).count()
        model_address = MemberAddress()
        model_address.member_id = member_info.id
        model_address.is_default = 1 if default_address_count == 0 else 0
        model_address.created_time = getCurrentDate()

    model_address.nickname = nickname
    model_address.mobile = mobile
    model_address.address = address
    model_address.province_id = province_id
    model_address.province_str = province_str
    model_address.city_id = city_id
    model_address.city_str = city_str
    model_address.area_id = district_id
    model_address.area_str = district_str
    model_address.updated_time = getCurrentDate()
    db.session.add(model_address)
    db.session.commit()
    return jsonify(resp)


@route_mini.route("/address/info")
def AddressInfo():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    member_info = g.member_info

    if id < 1 or  not member_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    address_info = MemberAddress.query.filter_by( id = id ).first()
    if not address_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    resp['data']['info'] = {
        "nickname": address_info.nickname,
        "mobile": address_info.mobile,
        "address": address_info.address,
        "province_id": address_info.province_id,
        "province_str": address_info.province_str,
        "city_id": address_info.city_id,
        "city_str": address_info.city_str,
        "dist_id": address_info.dist_id,
        "dist_str": address_info.dist_str
    }
    return jsonify(resp)


@route_mini.route("/address/ops", methods=["POST"])
def AddressOps():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    member_info = g.member_info

    if id < 1 or not member_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    address_info = MemberAddress.query.filter_by(id=id, member_id=member_info.id).first()
    if not address_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    if act == "del":
        address_info.status = 0
        address_info.updated_time = getCurrentDate()
        db.session.add(address_info)
        db.session.commit()
    elif act == "default":
        MemberAddress.query.filter_by(member_id=member_info.id)\
            .update({'is_default': 0})
        address_info.is_default = 1
        address_info.updated_time = getCurrentDate()
        db.session.add(address_info)
        db.session.commit()
    return jsonify(resp)




