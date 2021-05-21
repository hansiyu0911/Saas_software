import requests
import json
import logging
import pymysql
from sshtunnel import SSHTunnelForwarder


class saas1(object):

    # def __init__(self,user_id,cpy_id):
    #     self.user_id = user_id
        # self.product_id = product_id
        # self.cpy_id = cpy_id
    #     s = requests.session()
    #     self.s = s

    # 获取用户token
    def user_userid(self,user,passwd):
        url = "http://180.76.104.7:9538/prod-api/paas/mm/userlogin?md=010&cmd=001"
        heads = {"Content-Type": "application/json"}  # product_id
        data = {"a":user, "b": passwd}
        usertoken = requests.post(url=url, json=data, headers=heads)
        text = usertoken.text
        res = json.loads(text)

        user_id = res['b']
        # print(user_id)
        # logging.info('获取用户id')
        return user_id


    #获取用户cpy_id  15
    def login_info(self,user_id):
        url = "http://180.76.104.7:9538/prod-api/saas/res/login/info?md=057&cmd=120"
        heads = {"Content-Type": "application/json",
                 "user_id":f"{user_id}"}
        data = {}
        usercpyid = requests.get(url=url,headers=heads)
        text = usercpyid.text
        res = json.loads(text)

        cpy_id = res['d']['b']
        # print(self.cpy_id)
        return cpy_id

    #获取产品信息
    def user_product(self,user_id,product_id,cpy_id):
        url = "http://180.76.104.7:9538/prod-api/saas/res/product/list?md=057&cmd=042"
        heads = {"Content-Type": "application/json",
                 "user_id": f"{user_id}",
                 "product_id": f"{product_id}",
                 "cpy_id": f"{cpy_id}"
                 }
        data = {"a": "", "b": "", "c": "", "d": '', "e": "", "x": 1, "y": 10}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)
        # logging.info('获取产品信息')

        f = res['d'][0]['aa']  # 产品ID
        g = res['d'][0]['a']   # 产品名称
        # print(f,g)
        return f,g


    # 获取客户
    def user_client(self,user_id,product_id,cpy_id):
        url = "http://180.76.104.7:9538/prod-api/saas/res/customer/list?md=057&cmd=032"
        heads = {"Content-Type": "application/json",
                 "user_id": f"{user_id}",
                 "product_id": f"{product_id}",
                 "cpy_id": f"{cpy_id}"
                 }
        data = {"a": "", "b": "", "c": "", "d": "", "e": "", "x": 1, "y": 10}
        userclient = requests.post(url=url, json=data, headers=heads)
        test = userclient.text
        res = json.loads(test)
        # logging.info('获取客户信息')

        b = res['d'][0]['aa']  # 客户ID
        c = res['d'][0]['a']   # 客户名称
        d = res['d'][0]['c']   # 联系人
        e = res['d'][0]['d']   # 联系电话
        print(b,c,d,e)
        return b,c,d,e



    # 获取卸货坐标
    def user_coordinate(self,user_id,product_id,cpy_id):
        url = "http://180.76.104.7:9538/prod-api/saas/res/location/list?md=057&cmd=088"
        heads = {"Content-Type": "application/json",
                 "user_id": f"{user_id}",
                 "product_id": f"{product_id}",
                 "cpy_id": f"{cpy_id}"
                 }
        data = {"x": 1, "y": 10}
        usercoordinate = requests.post(url=url, json=data, headers=heads)
        test = usercoordinate.text
        res = json.loads(test)
        # logging.info('获取坐标信息')

        dizhi_a = res["d"][0]["aa"]  # 地址ID
        dizhi_b = res["d"][0]['d']  # 地址名称
        dizhi_e = res["d"][0]['a']  # 行政区域地址
        dizhi_f = res["d"][0]['b']  # 末端地址
        dizhi_g = res["d"][0]['c']  # 地址坐标
        # print(dizhi_a,dizhi_b,dizhi_e,dizhi_f,dizhi_g)
        return dizhi_a,dizhi_b,dizhi_e,dizhi_f,dizhi_g



    #发布订单
    def release_mainfest(self,user_id,product_id,cpy_id):
        saas = saas1()
        client = saas.user_client(user_id,product_id,cpy_id)
        product = saas.user_product(user_id,product_id,cpy_id)
        coordinate = saas.user_coordinate(user_id,product_id,cpy_id)
        url = "http://180.76.104.7:9538/prod-api/saas/gds/order/save/publish?md=057&cmd=065"
        heads = {"Content-Type": "application/json",
                 "user_id": f"{user_id}",
                 "product_id": f"{product_id}",
                 "cpy_id": f"{cpy_id}"
                 }
        data = {"b": client[0], "c": client[1], "d": client[2], "e": client[3],
                "f": product[0], "g": product[1], "h": "500000000", "i": "50000", "j": "161236812100",
                "k": "", "l":
                    [{"a": coordinate[0], "b": 2, "c": 1, "d": coordinate[1], "e": coordinate[2],
                      "f": coordinate[3], "g": coordinate[4], "h": "", "i": "50000", "k": "13978451231",
                      "l": "", "m": "", "n": ""},
                     {"a": coordinate[0], "b": 1, "c": 1, "d": coordinate[1], "e": coordinate[2],
                      "f": coordinate[3], "g": coordinate[4], "h": "", "i": "50000", "k": "15978789921",
                      "l": "", "m": "", "n": ""}]}
        usermainfest = requests.post(url=url, json=data, headers=heads)
        test = usermainfest.text
        res = json.loads(test)
        # logging.info('发布订单成功')
        # print(res)
        return res



    def MySqL(self,mainfest):
        with SSHTunnelForwarder(
                ('180.76.104.7', 22),
                ssh_password='Wcgj2018*',
                ssh_username='root',
                remote_bind_address=('192.168.0.10', 3306)) as server:
            conn = pymysql.connect(host='127.0.0.1',  # 本机host
                                   port=server.local_bind_port,
                                   user='root',
                                   passwd='123456',
                                   charset='utf8', )
            # print(conn)
            cur = conn.cursor()
            # cur.execute('show databases')
            cur.execute('use ftc_saas')
            cur.execute(f"DELETE FROM t_t_goods_order WHERE order_serial='{mainfest}'")
            conn.commit()
            print('删除成功')

















if __name__ == "__main__":
    a = saas1()
    a.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
    # a.user_userid()
    # a.user_product(428781,2025,15)
    # a.user_client(428868,2025,15)
    # a.user_coordinate(428781,2025,15)
    # a.release_mainfest(428868,2025,15)
