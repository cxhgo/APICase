#!/usr/bin/env python
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt
from API.config import setting
from API.lib.readexcel import ReadExcel
from API.lib.sendrequests import SendRequests
from API.lib.writeexcel import WriteExcel

# testData = ReadExcel(setting.Source_File, "Sheet1").read_data("Sheet1")
# testDatas = ReadExcel(setting.Source_File, "Sheet2").read_data("Sheet2")
# allDatas = testData+testDatas
#print(allDatas)
name = ["Sheet1","Sheet2"]
allData=[]
for i in range(len(name)):
    allData += ReadExcel(setting.Source_File, name[i]).read_data(name[i])
print(allData)
@ddt.ddt

class Demo_API(unittest.TestCase):
    """听芝心理-人格原型接口"""
    def setUp(self):
        #self.s = requests.session()
        print("测试开始")

    #@ddt.data(*testData)
    @ddt.data(*allData)
    def test_demoapi(self,data):

         #调用发送请求，获取响应判断，写入测试结果到表格
         #:param data:获取表格中所有接口的数据信息，每个接口数据执行一次
         #:return: 无


         # 获取ID字段数值，截取结尾数字并去掉开头0
         #print(data)
         rowNum = int(data['ID'].split("_")[2])
         sheetname =data['SheetName']
         #print(sheetname)
         #print(rowNum)
         # 发送请求
         #print(data)
         result = SendRequests().sendRequests(data)
         print(result)
         self.msg=result.get('msg')
         # if self.msg == None:
         #     self.msg = '空'
         print(self.msg)
         self.status=result.get('status_code')
         #print(self.status)
         #获取excel表格数据的状态码和消息
         readData_code = int(data["status_code"])
         readData_msg = data["msg"]
         print(readData_msg)
         if readData_msg =='':
            if readData_code == self.status:
               OK_data = "PASS"
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,OK_data)
            if readData_code != self.status:
               NOT_data = "FAIL"
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,NOT_data)
            self.assertEqual(self.status, readData_code, "返回实际结果是->:%s" % self.status)
         else:

            if readData_code == self.status and readData_msg == self.msg:
               OK_data = "PASS"
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,OK_data)
            if readData_code != self.status or readData_msg !=self.msg:
               NOT_data = "FAIL"
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,NOT_data)
            self.assertEqual(self.status, readData_code, "返回实际结果是->:%s" % self.status)
            self.assertEqual(self.msg, readData_msg, "返回实际结果是->:%s" %self.msg)

    def tearDown(self):
         print("测试结束")


if __name__ == "__main__":
    unittest.main()