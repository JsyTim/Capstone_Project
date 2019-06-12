# -*- coding: utf-8 -*-
from web.controllers.mini import route_mini
from flask import request, jsonify, g
from common.models.book.Book import Book
from common.models.member.MemberCart import MemberCart
from common.libs.cart.CartService import CartService
from common.libs.Helper import selectFilterObj, getDictFilterField
import json


@route_mini.route("/cart/index", methods=['GET', 'POST'])
def cartIndex():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "获取失败，未登录"
        return jsonify(resp)

    cart_list = MemberCart.query.filter_by(member_id=member_info.id).all()
    data_cart_list = []
    if cart_list:
        book_ids = selectFilterObj(cart_list, "book_id")
        book_map = getDictFilterField(Book, Book.book_id, "book_id", book_ids)
        for item in cart_list:
            tmp_book_info = book_map[item.book_id]
            tmp_data = {
                "id": item.id,
                "number": item.quantity,
                "book_id": item.book_id,
                "title": tmp_book_info.book_title,
                "price": str(round((float(tmp_book_info.book_oprice)*float(tmp_book_info.book_degrees)/10),2)),
                "main_image": str(tmp_book_info.book_main_image),
                "active": True
            }
            data_cart_list.append(tmp_data)
    resp['data']['list'] = data_cart_list
    return jsonify(resp)


@route_mini.route("/cart/set", methods=["GET", "POST"])
def setCart():
    resp = {'code': 200, 'msg': '添加购物车成功', 'data': {}}
    req = request.values
    book_id = int(req['id']) if 'id' in req else 0
    number = int(req['number']) if 'number' in req else 0
    if book_id < 1 or number < 1:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败"
        return jsonify(resp)

    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败"
        return jsonify(resp)

    book_info = Book.query.filter_by(book_id=book_id).first()
    if not book_info:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败"
        return jsonify(resp)

    if book_info.book_stock < number:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败,库存不足"
        return jsonify(resp)

    ret = CartService.setItems(member_id=member_info.id, book_id=book_info.book_id, number=number)
    if not ret:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败"
        return jsonify(resp)
    return jsonify(resp)


@route_mini.route("/cart/del", methods=["POST"])
def delCart():
    resp = {'code': 200, 'msg': '操作购物车成功', 'data': {}}
    req = request.values
    params_goods = req['goods'] if 'goods' in req else None

    items = []
    if params_goods:
        items = json.loads(params_goods)
    if not items or len(items) < 1:
        return jsonify(resp)

    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "删除购物车失败"
        return jsonify(resp)

    ret = CartService.deleteItem(member_id=member_info.id, items=items)
    if not ret:
        resp['code'] = -1
        resp['msg'] = "删除购物车失败"
        return jsonify(resp)
    return jsonify(resp)