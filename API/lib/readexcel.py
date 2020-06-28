# _*_ coding:utf-8 _*_
import xlrd

class ReadExcel():
    #-------------读取excel文件数据--------------
    def __init__(self,fileName,SheetName):
        self.data = xlrd.open_workbook(fileName)#打开excel读取文件，文件名有中文需要加r
        self.table = self.data.sheet_by_name(SheetName)#通过表名称获取表数据
        #------------获取总行数、总列数--------------
        self.rowsnum = self.table.nrows#获取表的有效行数
        self.colsnum = self.table.ncols#获取表的有效列数

    def read_data(self):
        if self.rowsnum> 1:
            #获取第一行的内容，列表格式
            keys = self.table.row_values(0)#返回由该行中所有单元格的数据类型组成的列表
            listApiData =[]
            #获取每一行的内容，列表格式
            for col in range(1,self.rowsnum):
                values = self.table.row_values(col)
                #keys,values组合转换为字典
                api_dict = dict(zip(keys,values))#将keys和values打包为元组对象，并转化为dict
                listApiData.append(api_dict)
            return listApiData
            #return api_dict
        else:
            print("表格为空！")
            return None