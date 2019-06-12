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
    book_info = Book.query.filter_by(book_isbn13=isbn).first()
    if book_info:
        resp['data'] = {
            "id": book_info.book_id,
            "title": book_info.book_title,
            "author": book_info.book_author,
            "price": str(book_info.book_price),
            "oprice": str(book_info.book_oprice),
            'main_image': book_info.book_main_image,
            'grade': str(round(book_info.book_grade, 1)),
        }
        return jsonify(resp)
    else:
        book_info = BookService.getBookInfo(str(isbn))
        discount = 0.3
        # discount = BookService.caldiscount(book_info.book_author)
        if not book_info:
            resp['code'] = -1
            resp['msg'] = "无法获取图书信息"
            return jsonify(resp)
        elif float(book_info['rating']['average']) < 7.0:
            resp['code'] = -1
            resp['msg'] = "此书不收"
            return jsonify(resp)
        else:
            resp['data'] = {
                "title": book_info['title'],
                "author": book_info['author'],
                "price": str(float(book_info['price'])*float(discount)),
                'main_image': book_info['image'],
                'grade': str(book_info['rating']['average'])
            }
    return jsonify(resp)