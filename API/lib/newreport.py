# _*_ coding:utf-8 _*_
import os


def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    #返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(testreport)
    #print(lists)
    #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    #最后对lists元素，按文件修改时间大小从小到大排序。
    #获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    lists.sort(key = lambda fn:os.path.getmtime(testreport +"\\"+fn))
    #连接testreport和list[-1]的值
    file_new = os.path.join(testreport,lists[-1])
    return file_new

#print(new_report('F:\\工作\\自动化\\interface\\API\\report'))#调试使用