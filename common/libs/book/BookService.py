# -*- coding: utf-8 -*-
import requests, json
from common.models.book.Book import Book
from application import app, db
from common.models.book.BookStockChangeLog import BookStockChangeLog
from common.libs.Helper import getCurrentDate
class BookService():

    @staticmethod
    def getBookDetailInfo(barcode):
        url = 'https://douban.uieee.com/v2/book/isbn/' + barcode
        r = requests.get(url)
        res = json.loads(r.text)
        if res is None:
            return "无法获取图书详情信息"
        return res

    @staticmethod
    def setStockChangeLog(book_id=0, quantity=0, note=''):

        if book_id < 1:
            return False

        book_info = Book.query.filter_by(book_id=book_id).first()
        if not book_info:
            return False

        model_stock_change = BookStockChangeLog()
        model_stock_change.bood_id = book_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = book_info.book_stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True