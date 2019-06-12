# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_isbn13 = db.Column(db.String(13), nullable=False, server_default=db.FetchedValue())
    book_title = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue())
    book_author = db.Column(db.String(80), nullable=False, server_default=db.FetchedValue())
    book_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    book_oprice = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    book_main_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    book_grade = db.Column(db.Float(asdecimal=True))
    book_press = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue())
    book_binding = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue())
    book_desc = db.Column(db.Text)
    book_degrees = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue())
    book_stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tags = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    book_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_month_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_total_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    book_updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    book_created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    book_recomm_image = db.Column(db.String(1000), server_default=db.FetchedValue())
