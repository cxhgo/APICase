# _*_ coding:utf-8 _*_
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)
from API.config import setting
from pymysql import connect,cursors
from pymysql import  OperationalError
import configparser as oparser


#-------------读取配置文件，进行增删改查--------------
cf= oparser.ConfigParser()#创建对象
cf.read(setting.Test_Config,encoding="UTF-8")#读取配置文件中参数
host = cf.get("mysqlconf","host")#为指定的section获取一个选项值
port = cf.get("mysqlconf","port")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
db = cf.get("mysqlconf","db_name")
print(cf)
print(host)

class DB:
    #-------------mysql基本操作--------------
    def __init__(self):
        try:
            #连接数据库
            self.conn = connect(host = host,
                                user = user,
                                password = password,
                                db = db,
                                charset = "utf8mb4",#utf8的超集，兼容四字节的unicode
                                cursorclass =cursors.DictCursor#返回字典类型数据：{键:值}
                                )
        except OperationalError as e:
            print("Mysql Error %d:%s" %(e.args[0],e.args[1]))
    #清除表数据
    def clear(self,table_name):
        real_sql = "delete from"+table_name+";"
        with self.conn.cursor() as cursor:
            #取消表的外键约束
            cursor.execute("SET FROMIGN_KEY_CHECK=0;")
            cursor.execute(real_sql)#执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
        self.conn.commit()#缓存后统一提交，查询语句不需要缓存，增删改需要，添加和提交中间如果有查询语句，会出现阻塞，查询会等提交后再查询
        cursor.close()

    #插入表数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] ="'"+str(table_data[key])+"'"
        key =','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO"+table_name +"("+ key +")VALUES("+ value +")"
        with self.conn.cursor()as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
        cursor.close()

    #关闭数据库
    def close(self):
        self.conn.close()

    #初始化数据
    def init_data(self,datas):
        #datas.items()以列表返回可遍历的(键, 值) 元组数组
        for table,data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table,d)
        self.close()
