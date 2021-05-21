import requests
import json
import csv
import re
import pymysql
from sshtunnel import SSHTunnelForwarder


# class saas(object):

# 获取用户token
def user_token(self,url,headers,data):
    url = "http://180.76.104.7:9538/prod-api/paas/mm/userlogin?md=010&cmd=001"
    heads = {"Content-Type": "application/json"}  # product_id
    data = {"a": 15037819972, "b": "e10adc3949ba59abbe56e057f20f883e"}
    usertoken = requests.post(url=url, json=data, headers=heads)
    text = usertoken.text
    token = json.loads(text)
    return token
        # print(token)

        # log_info:cpy_id(头部去拿)
        # 函数封装
        # 接口返回值

        # return usertoken.json()
        # print(usertoken.text)
        # print(usertoken.status_code)

#获取cpy_id
def login_info():
    url = "http://180.76.104.7:9538/prod-api/saas/res/login/info?md=057&cmd=120"
    heads = {"Content-Type": "application/json",
             "user_id":"428781"}
    data = {}
    usercpyid = requests.get(url=url,headers=heads)
    text = usercpyid.text
    user_cpyid = json.loads(text)
    return user_cpyid
    # print(user_cpyid)






#获取客户
def user_client():
    url = "http://180.76.104.7:9538/prod-api/saas/res/customer/list?md=057&cmd=032"
    heads = {"Content-Type": "application/json",
             "user_id": "428781",
             "product_id": "2025",
             "cpy_id": "15"
             }
    data = {"a": "", "b": "", "c": "", "d": "", "e": "", "x": 1, "y": 10}
    userclient = requests.post(url=url, json=data, headers=heads)
    test = userclient.text
    client = json.loads(test)

    b = client['d'][0]['aa'] # 客户ID
    c = client['d'][0]['a']  # 客户名称
    d = client['d'][0]['c']  # 联系人
    e = client['d'][0]['d']  # 联系电话
    # print(b)
    return [b, c, d, e]
    # return userclient.json()
    # print(userclient.text)
    # print(userclient.status_code)


# 获取产品
def user_product():
    url = "http://180.76.104.7:9538/prod-api/saas/res/product/list?md=057&cmd=042"
    heads = {"Content-Type": "application/json",
             "user_id": "428781",
             "product_id": "2025",
             "cpy_id": "15"
             }
    data = {"a": "", "b": "", "c": "", "d": '', "e": "", "x": 1, "y": 10}
    userproduct = requests.post(url=url, json=data, headers=heads)
    test = userproduct.text
    product = json.loads(test)

    f = product['d'][0]['aa']  # 产品ID
    g = product['d'][0]['a']   # 产品名称

    return [f, g]

    # return  userroute.json()
    # print(userroute.text)
    # print(userroute.status_code)


# 获取卸货坐标
def user_coordinate():
    url = "http://180.76.104.7:9538/prod-api/saas/res/location/list?md=057&cmd=088"
    heads = {"Content-Type": "application/json",
             "user_id": "428781",
             "product_id": "2025",
             "cpy_id": "15"
             }
    data = {"x": 1, "y": 10}
    usercoordinate = requests.post(url=url, json=data, headers=heads)
    test = usercoordinate.text
    coordinate = json.loads(test)

    dizhi_a = coordinate["d"][0]["aa"]  # 地址ID
    dizhi_b = coordinate["d"][0]['d']  # 地址名称
    dizhi_e = coordinate["d"][0]['a']  # 行政区域地址
    dizhi_f = coordinate["d"][0]['b']  # 末端地址
    dizhi_g = coordinate["d"][0]['c']  # 地址坐标

    return [dizhi_a, dizhi_b, dizhi_e, dizhi_f, dizhi_g]

    # return usercoordinate.json()
    # print(usercoordinate.text)
    # print(usercoordinate.status_code)


# 获取装货地址


# 发布订单
def release_mainfest():
    url = "http://180.76.104.7:9538/prod-api/saas/gds/order/save/publish?md=057&cmd=065"
    heads = {"Content-Type": "application/json",
             "user_id": "428781",
             "product_id": "2025",
             "cpy_id": "15"
             }
    data = {"b": user_client()[0], "c": user_client()[1], "d": user_client()[2], "e": user_client()[3],
            "f": user_product()[0], "g": user_product()[1], "h": "500000000", "i": "50000", "j": "161236812100",
            "k": "", "l":
                [{"a": user_coordinate()[0], "b": 2, "c": 1, "d": user_coordinate()[1], "e": user_coordinate()[2],
                  "f": user_coordinate()[3], "g": user_coordinate()[4], "h": "", "i": "50000", "k": "13978451231",
                  "l": "", "m": "", "n": ""},
                 {"a": user_coordinate()[0], "b": 1, "c": 1, "d": user_coordinate()[1], "e": user_coordinate()[2],
                  "f": user_coordinate()[3], "g": user_coordinate()[4], "h": "", "i": "50000", "k": "15978789921",
                  "l": "", "m": "", "n": ""}]}
    usermainfest = requests.post(url=url, json=data, headers=heads)
    test = usermainfest.text
    mainfest = json.loads(test)
    # print(mainfest)
    # num = mainfest['m'].replace("货单编号",'').replace(":","")
    num = re.findall("货单编号.(.*)?", mainfest["m"])
    # 函数内部不做任何筛选
    print(num[0])
    return num[0]


    # print(release_mainfest())


    # print(user_client())
    # print(user_product())
    # print(user_coordinate())


if __name__ == "__main__":


    # user_token()
    # login_info()
    # user_client()
    # user_product()
    # user_coordinate()
    release_mainfest()

