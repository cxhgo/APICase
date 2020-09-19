# _*_ coding:utf-8 _*_
import os,sys
#sys.path.append(os.path.dirname(__file__))
from API.config import setting
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from API.lib.newreport import new_report
from API.package.HTMLTestRunnerone import HTMLTestRunner
from API.testcase.testAPI import Demo_API
from API.lib.sendmail import send_mail
def add_case(test_path = setting.Test_Case):
    """
         加载所有的测试用例
         :param test_path:加载用例的路径
         :return: 返回测试套件
    """
    discover = unittest.defaultTestLoader.discover(test_path,pattern='test*.py')#批量调用setting.Test_Case路径下的文件，返回一个测试套件
    print(discover)
    return discover



def run_case(all_case,result_path=setting.Test_Report):
    """
         执行所有的测试用例
         :param all_case:测试套件
         :param result_path：生成报告保存路径
         :return: 无
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path+'/'+now+'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='接口自动化测试报告',
                            tester='归乐'
                            )
    runner.run(all_case)

    fp.close()
    report = new_report(setting.Test_Report)#调用模块生成最新报告
    send_mail(report)#发送邮件

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)
