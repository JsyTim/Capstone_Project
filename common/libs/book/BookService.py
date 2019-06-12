# -*- coding: utf-8 -*-
import requests, json
from common.models.book.Book import Book
from application import app, db
from common.models.book.BookStockChangeLog import BookStockChangeLog
from common.libs.Helper import getCurrentDate
import logging
from gensim import models
from sqlalchemy import or_


class BookService():
    @staticmethod
    def getBookInfo(barcode):
        url = 'https://douban.uieee.com/v2/book/isbn/' + barcode
        r = requests.get(url)
        res = json.loads(r.text)
        if res is None:
            print("无法获取图书详情信息")
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
        model_stock_change.book_id = book_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = book_info.book_stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True

    @staticmethod
    def trainModel(param):
        logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
        model = models.Word2Vec.load("G:/model/wiki_corpus.model")
        one_corpus = [param]
        # 输入一个词找出相似的前10个词
        result = model.most_similar(one_corpus[0], topn=10)
        # 将返回的结果转换为字典
        res = dict()
        for sim in result:
            res[sim[0]] = sim[1]
        return res

    @staticmethod
    def caldiscount(author):
        discount = 0.3
        res = BookService.trainModel(author)
        authors = []
        for key in res:
            authors.append(key)
        for author in authors:
            book_info = Book.query.filter_by(book_author=author).first()
            if not book_info:
                continue
            else:
                discount = book_info.degree
                return discount
        return discount

    @staticmethod
    def calsimilar(mix_kw):
        res = BookService.trainModel(mix_kw)
        kws = []
        book_images = []
        for key in res:
            kws.append(key)
        for kw in kws:
            query = Book.query
            rule = or_(Book.book_title.ilike("%{0}%".format(mix_kw)), Book.book_author.ilike("%{0}%".format(mix_kw)), Book.tags.ilike("%{0}%".format(mix_kw)))
            book_info = query.filter(rule).order_by(Book.book_total_count, Book.book_id).limit(3).all()
            if not book_info:
                continue
            else:
                book_images.append(book_info.book_main_image)
                if len(book_images) > 3:
                    break
        if len(book_images) < 1:
            return "暂无推荐"
        return book_images