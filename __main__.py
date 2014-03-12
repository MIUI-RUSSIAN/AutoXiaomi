# -*- coding: utf-8 -*- #!/usr/bin/python

import threading
import os,sys,time,random
from time import gmtime, strftime
from module_xiaomi import Xiaomi

class buyThread (threading.Thread):
	
	def __init__(self, threadID):
		random.seed(time.time())
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		xiaomi = Xiaomi()
		logined = xiaomi.login('[Account]','[Password]')
		if (not logined == True):
			self.cout( xiaomi.email + ' login failure')
			return
		self.cout( xiaomi.email + ' is logined')
		while(True):
			bres = xiaomi.buy_method1(2130100011)
			if (bres == True):
				self.cout('Order successfully , oreder-id : ' + str(bres))
			else:
				self.cout(xiaomi.err)
			time.sleep(random.random() * 10000000000000000 % 5 + 1.9)

		

	def cout(self,text):
		print strftime("[Thread"+str(self.threadID)+"][%Y-%m-%d %H:%M:%S]: " + text + "" , gmtime())

print 'Xiaomi Dianyuan Plugin ver 1.0'
print 'Author : ms890110'

t1 = buyThread(1)
t2 = buyThread(2)

t1.start()
t2.start()
