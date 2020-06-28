# _*_ coding:utf-8 _*_
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests

class SendRequests():
    def sendRequests(self,apiData):
        try:
            #发送请求数据
            method = apiData["method"]
            #print(method)
            url = apiData["url"]
            #print(url)
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
                #print(par)
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
                #print(h)
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])

            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
                #print(body)
            elif type == "json":
                body =json.dumps(body_data)
                #print(body)
            else:
                body = body_data
                #print(body)
            re =requests.request(method=method,url =url, headers =h,params = par,data = body,verify = v)
            msg = json.loads(re.text)
            msg['status_code']=re.status_code
            print(msg)
            print(re.status_code)
            return msg
            #print(re.text)
            # if method =="get":
            #    re = s.get(url =url, headers =h,params = par,data = body,verify = v)
            #    print(re.text)
            #    return re
            # elif method == "post":
            #    re = s.post(url =url, headers =h,params = par,data = body,verify = v)
            #    print(re.text)
            #    return re
        except Exception as e:
            print(e)