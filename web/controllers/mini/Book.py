from web.controllers.mini import route_mini
from flask import request, jsonify, g
from common.libs.book.BookService import BookService
from application import db
from common.models.book.Book import Book
from common.models.book.BookCat import BookCat
from common.models.member.MemberComments import MemberComments
from common.libs.Helper import getCurrentDate, getDictFilterField,selectFilterObj
from sqlalchemy import or_
from common.libs.UrlManager import UrlManager
from common.models.member.MemberCart import MemberCart
from common.models.member.Member import Member


@route_mini.route("/book/index", methods=['GET', 'POST'])
def bookIndex():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    book_list = Book.query.filter_by(book_status=1)\
        .order_by(Book.book_total_count.desc(), Book.book_id.desc()).limit(20).all()

    data_book_list = []
    if book_list:
        for item in book_list:
            tmp_data = {
                'id': item.book_id,
                'title': str(item.book_title),
                'price': str(item.book_price),
                'oprice': str(item.book_oprice),
                'author': item.book_author,
                'grade': str(round(item.book_grade, 1)),
                'main_image': item.book_main_image,
                'tag': item.tags
            }
            data_book_list.append(tmp_data)

    resp['data']['book_list'] = data_book_list
    return jsonify(resp)


@route_mini.route("/book/info", methods=['GET', 'POST'])
def bookInfo():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    book_info = Book.query.filter_by(book_id=id).first()
    if not book_info or book_info.book_status == 0:
        resp['code'] = -1
        resp['msg'] = "图书已下架"
        return jsonify(resp)

    # member_info = g.member_info
    # cart_number = 0
    # if member_info:
    #     cart_number = MemberCart.query.filter_by(member_id=member_info.id).count()
    resp['data'] = {
        "id": book_info.book_id,
        "title": book_info.book_title,
        "author": book_info.book_author,
        "price": str(book_info.book_price),
        "oprice": str(book_info.book_oprice),
        'main_image': book_info.book_main_image,
        'grade': str(round(book_info.book_grade, 1)),
        "press": book_info.book_press,
        "binding": book_info.book_binding,
        "desc": book_info.book_desc,
        "stock": book_info.book_stock,
        "tags": book_info.tags,
        "total_count": book_info.book_total_count,
        "comment_count": book_info.book_comment_count,

    }
    # resp['data']['cart_number'] = cart_number
    return jsonify(resp)


@route_mini.route("/book/comments")
def bookComments():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    query = MemberComments.query.filter(MemberComments.book_ids.ilike("%_{0}_%".format(id)))
    list = query.order_by(MemberComments.id.desc()).limit(5).all()
    data_list = []
    if list:
        member_map = getDictFilterField(Member, Member.id, "id", selectFilterObj(list, "member_id"))
        for item in list:
            if item.member_id not in member_map:
                continue
            tmp_member_info = member_map[item.member_id]
            tmp_data = {
                'score': item.score_desc,
                'date': item.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                "content": item.content,
                "user": {
                    'nickname': tmp_member_info.nickname,
                    'avatar_url': tmp_member_info.avatar,
                }
            }
            data_list.append(tmp_data)
    resp['data']['list'] = data_list
    resp['data']['count'] = query.count()
    return jsonify(resp)