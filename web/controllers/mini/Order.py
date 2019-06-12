# -*- coding: utf-8 -*-
from web.controllers.mini import route_mini
from flask import request, jsonify,g
from application import app, db
import json, decimal
from common.models.book.Book import Book
from common.models.member.Member import Member
from common.models.member.MemberAddress import MemberAddress
from common.models.pay.PayOrder import PayOrder
from common.libs.UrlManager import UrlManager
from common.libs.Helper import getCurrentDate
from common.libs.pay.PayService import PayService
# from common.libs.pay.WeChatService import WeChatService
from common.libs.cart.CartService import CartService
from common.models.member.OauthMemberBind import OauthMemberBind


@route_mini.route("/order/info", methods=["GET", "POST"])
def orderInfo():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    params_goods = req['goods'] if 'goods' in req else None
    member_info = g.member_info
    params_goods_list = []
    if params_goods:
        params_goods_list = json.loads(params_goods)

    book_dic = {}
    for item in params_goods_list:
        book_dic[str(item['id'])] = item['number']
    book_ids = book_dic.keys()
    book_list = Book.query.filter(Book.book_id.in_(book_ids)).all()
    data_book_list = []
    yun_price = pay_price = decimal.Decimal(0.00)
    if book_list:
        for item in book_list:
            tmp_data = {
                "id": item.book_id,
                "title": item.book_title,
                "price": str(item.book_price),
                'main_image': str(item.book_main_image),
                'number': book_dic[str(item.book_id)]
            }
            pay_price = pay_price + item.book_price * int(book_dic[str(item.book_id)])
            data_book_list.append(tmp_data)
    # 获取地址
    address_info = MemberAddress.query.filter_by(is_default=1, member_id=member_info.id, status=1).first()
    default_address = ''
    if address_info:
        default_address = {
            "id": address_info.id,
            "name": address_info.nickname,
            "mobile": address_info.mobile,
            "address": "%s%s%s%s"%(address_info.province_str, address_info.city_str, address_info.dist_str, address_info.address )
        }
    resp['data']['book_list'] = data_book_list
    resp['data']['pay_price'] = str(pay_price)
    resp['data']['yun_price'] = str(yun_price)
    resp['data']['total_price'] = str(pay_price + yun_price)
    resp['data']['default_address'] = default_address
    return jsonify(resp)


@route_mini.route("/order/create", methods=["GET", "POST"])
def orderCreate():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    type = req['type'] if 'type' in req else ''
    note = req['note'] if 'note' in req else ''
    express_address_id = int(req['express_address_id']) if 'express_address_id' in req and req['express_address_id'] else 0
    params_goods = req['goods'] if 'goods' in req else None

    items = []
    if params_goods:
        items = json.loads(params_goods)
    print(items)
    print(params_goods)
    if len(items) < 1:
        resp['code'] = -1
        resp['msg'] = "下单失败：没有选择商品"
        return jsonify(resp)

    address_info = MemberAddress.query.filter_by(id=express_address_id).first()
    if not address_info or not address_info.status:
        resp['code'] = -1
        resp['msg'] = "下单失败：快递地址无效"
        return jsonify(resp)

    member_info = g.member_info
    target = PayService()
    params = {
        "note": note,
        'express_address_id': address_info.id,
        'express_info': {
            'mobile': address_info.mobile,
            'nickname': address_info.nickname,
            "address": "%s%s%s%s"%(address_info.province_str, address_info.city_str, address_info.dist_str, address_info.address)
        }
    }
    resp = target.createOrder(member_info.id, items, params)

    #下单成功后将下单的商品去掉
    if resp['code'] == 200 and type == "cart":
        CartService.deleteItem(member_info.id, items)

    return jsonify(resp)


@route_mini.route("/order/pay", methods=["GET", "POST"])
def orderPay():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    member_info = g.member_info
    req = request.values
    order_sn = req['order_sn'] if 'order_sn' in req else ''
    pay_order_info = PayOrder.query.filter_by(order_sn=order_sn, member_id=member_info.id).first()
    if not pay_order_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙。请稍后再试~~"
        return jsonify(resp)

    oauth_bind_info = OauthMemberBind.query.filter_by(member_id=member_info.id).first()
    if not oauth_bind_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙。请稍后再试~~"
        return jsonify(resp)

    pay_order_info.status = 1
    db.session.add(pay_order_info)
    db.session.commit()
    return jsonify(resp)


@route_mini.route("/order/ops", methods=["POST"])
def orderOps():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    member_info = g.member_info
    order_sn = req['order_sn'] if 'order_sn' in req else ''
    act = req['act'] if 'act' in req else ''
    pay_order_info = PayOrder.query.filter_by(order_sn=order_sn, member_id=member_info.id).first()
    if not pay_order_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙。请稍后再试~~"
        return jsonify(resp)

    if act == "cancel":
        target_pay = PayService()
        ret = target_pay.closeOrder(pay_order_id=pay_order_info.id)
        if not ret:
            resp['code'] = -1
            resp['msg'] = "系统繁忙。请稍后再试~~"
            return jsonify(resp)
    elif act == "confirm":
        pay_order_info.express_status = 1
        pay_order_info.updated_time = getCurrentDate()
        db.session.add(pay_order_info)
        db.session.commit()

    return jsonify(resp)




