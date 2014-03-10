import urllib
import urllib2
import cookielib
import pickle


class HttpRequest:


    def __init__(self):
        
        self.cookies = cookielib.CookieJar()
        self.init() 

    def init(self):
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener.addheaders += [('Content-Type'\
        ,'application/x-www-form-urlencoded')]
        self.opener.addheaders += [('Accept-Language'\
        ,'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4')]
        self.opener.addheaders += [('User-agent'\
        ,'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36')]

    def post(self ,url ,post_data, headers = None):
        
        post_data = urllib.urlencode(post_data);
        res = self.opener.open(url, post_data,headers)
        return res.read()

    def get(self ,url , headers = None):
       
        if headers != None:
            res = self.opener.open(url)
        else:
            res = self.opener.open(url,None,headers)
        return res.read()
        
    def addheader(self ,header):
        
        self.opener.addheaders += header

    def save_cookies(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.cookies, f)

    def load_cookies(self, filename):
        with open(filename, 'rb') as f:
            self.cookies =  pickle.load(f)

