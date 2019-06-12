from web.controllers.mini import route_mini
from flask import request, jsonify, g
from common.libs.book.BookService import BookService
from application import db
from common.models.book.Book import Book
from common.models.book.BookCat import BookCat
from common.libs.Helper import getCurrentDate, getDictFilterField,selectFilterObj
from sqlalchemy import or_
from common.libs.UrlManager import UrlManager
from common.models.member.Member import Member


@route_mini.route("/scan/index", methods=['GET', 'POST'])
def scan():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    isbn = int(req['isbn']) if 'isbn' in req else 0
    print(isbn)
    # book_info = Book.query.filter_by(book_id=id).first()
    # if not book_info or book_info.book_status == 0:
    #     resp['code'] = -1
    #     resp['msg'] = "图书已下架"
    #     return jsonify(resp)
    #
    # resp['data'] = {
    #     "id": book_info.book_id,
    #     "title": book_info.book_title,
    #     "author": book_info.book_author,
    #     "price": str(book_info.book_price),
    #     "oprice": str(book_info.book_oprice),
    #     'main_image': book_info.book_main_image,
    #     'grade': str(round(book_info.book_grade, 1)),
    #     "press": book_info.book_press,
    #     "binding": book_info.book_binding,
    #     "desc": book_info.book_desc,
    #     "stock": book_info.book_stock,
    #     "tags": book_info.tags,
    #     "total_count": book_info.book_total_count,
    #     "comment_count": book_info.book_comment_count,
    # }
    return jsonify(resp)