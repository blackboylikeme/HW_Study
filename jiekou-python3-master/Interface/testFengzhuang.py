# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
from Public.test_requests import requ
reques=requ()
class TestApi(object):
	def __init__(self,url,key,content,fangshi):
		self.url=url
		self.key=key
		self.content=content
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi=='POST':
			self.parem = {'key': self.key, 'info': self.content}
			self.response=reques.post(self.url,self.parem)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.content}
			self.response = reques.get(url=self.url,params=self.parem)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		return json_data