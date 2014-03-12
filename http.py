# -*- coding: utf-8 -*-
''' http.py

    HttpRequest()

    Methods :
        post ( url , data , headers )
        get ( url , headers )
'''        

import urllib
import urllib2
import cookielib
import pickle


class HttpRequest:


    def __init__(self):
        
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener.addheaders += [('Content-Type'\
                ,'application/x-www-form-urlencoded')]
        self.opener.addheaders += [('Accept-Language'\
                ,'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4')]
        self.opener.addheaders += [('User-agent'\
                ,'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36')]

    '''
        desc: post data to web
        params:
            url : website's location
            post_data : the data you wanna to post , like
                { 'a' : '1' ,,,}
            headers : if you want to add any header , you can put like
                { 'User-Agen' : '......',... )
    '''
    def post(self ,url ,post_data, headers = None):
        
        post_data = urllib.urlencode(post_data);
        res = self.opener.open(url, post_data,headers)
        return res.read()

    '''
        desc: get Web Conent
        params:
            url : website's location
            headers : if you want to add any header , you can put like
                { 'User-Agen' : '......',... )
    '''
    def get(self ,url , headers = None):
       
        if headers != None:
            res = self.opener.open(url)
        else:
            res = self.opener.open(url,None,headers)
        return res.read()

    def addheader(self ,header):
        
        self.opener.addheaders += header

    '''
        desc: save current cookies to file
    '''
    def save_cookies(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.cookies, f)

    '''
        desc: load current cookies from file
    '''
    def load_cookies(self, filename):
        with open(filename, 'rb') as f:
            self.cookies =  pickle.load(f)

