# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class BookCat(db.Model):
    __tablename__ = 'book_cat'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(32), nullable=False)
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
