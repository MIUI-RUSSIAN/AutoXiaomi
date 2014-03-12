# -*- coding: utf-8 -*-
#!/usr/bin/python

import os,sys
import http
import re
import ast
import json

class Xiaomi:

    def __init__(self):

        self.req = http.HttpRequest()

    def login(self ,email ,password):

        self.uid = None
        self.email = email
        self.password = password
        login_page = self.req.get('https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fwww.xiaomi.tw%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fwww.xiaomi.tw%26sign%3DZDM4ODcwNWFiYzMzZjk3MWZjMWRmZmEyNmVkODE3MmE0NDZmMWY2ZQ%2C%2C&sid=xiaomitw&_locale=zh_TW')

        callback = re.search('callback = encodeURIComponent\("(.*)"\)',login_page).group(1)
        sign = re.search('sign = encodeURIComponent\("(.*)"\)',login_page).group(1)
        sid  = 'xiaomitw'
        qs   = re.search('qs = encodeURIComponent\("(.*)"\)',login_page).group(1)
        
        payload = {
                'user':email,
                'pwd':password,
                'callback':callback,
                'qs':qs,
                '_sign':sign,
                '_json':'true',
                'sid':sid
            }

        login_response = self.req.post('https://account.xiaomi.com/pass/serviceLoginAuth2'\
                                       ,payload)
        logined = re.search('"desc":"成功"',login_response)
        if (logined == None):
            return False

        login_json = unicode(login_response, "utf-8")
        login_json = json.loads(login_json.replace(u'&&&START&&&',''))
        
        self.req.get(login_json['location'])
        
        self.uid = login_json['userId']

        return True


    def get_uid(self):
        if ( self.uid != None ):
            return self.uid
        return None

    def buy_method1(self, itemid):
        itemid = str(itemid)
        if ( self.uid != None ):
            add_page = self.req.get('http://www.xiaomi.tw/cart/add/' + itemid + '-0-2')
            try:
                if ( re.search('商品沒有庫存了' , add_page) != None):
                    self.err = 'Out of stock.'
                    return False
                if ( os.path.isfile('buy.config')):
                    
                    config = open('buy.config','r').read().decode('utf-8-sig')
                    config = ast.literal_eval(config)

                    confirm_page = self.req.post('http://www.xiaomi.tw/buy/checkout',config)   
                    order_id = re.search('var order_id="(.*)";;',confirm_page).group(1)
                    
                    return order_id

            except:
                self.err = 'Exception occuered'
                return False
            
    
