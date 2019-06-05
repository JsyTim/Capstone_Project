# -*- coding: utf-8 -*-
import hashlib
import base64
import random
import string


class AdminService():

    @staticmethod
    def geneAuthCode(admin_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (admin_info.aid, admin_info.login_name, admin_info.login_pwd, admin_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join( keylist))
