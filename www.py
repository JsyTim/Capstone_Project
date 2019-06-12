# -*- coding: utf-8 -*-
from application import app

'''
Interceptor
'''
from web.interceptors.AuthInterceptor import *
from web.interceptors.ApiAuthInterceptor import  *
from web.interceptors.ErrorInterceptor import  *


'''
Blueprint: register for every router
'''
from web.controllers.index import route_index
from web.controllers.admin.Admin import route_admin
from web.controllers.static import route_static
from web.controllers.account.Account import route_account
from web.controllers.book.Book import route_book
from web.controllers.member.Member import route_member
from web.controllers.finance.Finance import route_finance
from web.controllers.stat.Stat import route_stat
from web.controllers.mini import route_mini
from web.controllers.upload.Upload import route_upload
from web.controllers.chart import route_chart

app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_admin, url_prefix="/admin")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_account, url_prefix="/account")
app.register_blueprint(route_book, url_prefix="/book")
app.register_blueprint(route_member, url_prefix="/member")
app.register_blueprint(route_finance, url_prefix="/finance")
app.register_blueprint(route_stat, url_prefix="/stat")
app.register_blueprint(route_mini, url_prefix="/mini")
app.register_blueprint(route_upload, url_prefix="/upload")
app.register_blueprint(route_chart, url_prefix="/chart")