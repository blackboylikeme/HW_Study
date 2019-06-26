# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
# @Notes   : liyiteng
import xlrd
from Public.log  import LOG,logger
@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[0] #获取第一个表格对象
        nrows=me.nrows #获取行数
        listid=[]
        listkey=[]
        listconeent=[]
        listurl=[]
        listfangshi=[]
        listqiwang=[]
        listrelut=[]
        listname=[]
        for i in range(1,nrows):
            listid.append(me.cell(i,0).value)#append用例ID-用例id列表
            listkey.append(me.cell(i,2).value)#获取key
            listconeent.append(me.cell(i,3).value)#获取参数
            listurl.append(me.cell(i,4).value)#获取URL
            listname.append(me.cell(i,1).value)#获取用例名
            listfangshi.append((me.cell(i,5).value))#请求方式 POST or Get
            listqiwang.append((me.cell(i,6).value))#期望值
        return listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname  #返回列值列表
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return