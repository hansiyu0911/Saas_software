import requests
import json
import logging
import csv
import pymysql
from common.test import saas1
# from common.faker_test import car_number,trailer_number

def product_shuju():
    csv_shuju = []
    with open('../date/aaa.csv','r',encoding='utf-8') as f :
        read = csv.reader(f)
        print(read)

class  saas_client(object):
        '''客户管理'''

        def __init__(self):
            self.saas = saas1()
            self.user_id = self.saas.user_userid(15137819972, 'e10adc3949ba59abbe56e057f20f883e')
            self.product_id = 2025
            self.cpy_id = self.saas.login_info(self.user_id)
            self.url = "http://180.76.104.7:9538/prod-api"
            self.headers = {"Content-Type": "application/json",
                            "user_id": f"{self.user_id}",
                            "product_id": f"{self.product_id}",

                            "cpy_id": f"{self.cpy_id}"
                            }

        # 客户新增
        def add_client(self):
            url = f"{self.url}/saas/res/customer/add?md=057&cmd=033"
            heads = self.headers
            data = {"a": "客户名称", #客户名称
                    "b": "1",#客户类型  1货主，2车队，3货主车队
                    "c": "联系人",#联系人
                    "d":"15037819972",#手机号码
                    "e": "江苏省南京市浦口区永宁街道小刘队"}#客户地址
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 客户查询
        def detail_client(self,aa):
            url = f"{self.url}/saas/res/customer/detail?md=057&cmd=034"
            heads = self.headers
            data = {"aa": aa}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 客户修改
        def modify_client(self,aa):
            url = f"{self.url}/saas/res/customer/modify?md=057&cmd=035"
            heads = self.headers
            data = {"a": "客户名称1",
                    "aa": aa,
                    "b": "2",
                    "c": "联系人2",
                    "d": '15137819972',
                    "e": "河南省开封市鼓楼区",}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 客户删除
        def remove_client(self,aa):
            url = f"{self.url}/saas/res/customer/remove?md=057&cmd=036"
            heads = self.headers
            data = {"aa": aa}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res
class  saas_product(object):

    '''产品管理'''
    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id  = self.saas.login_info(self.user_id)
        self.url     = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                 "user_id": f"{self.user_id}",
                 "product_id": f"{self.product_id}",
                 "cpy_id": f"{self.cpy_id}"
                 }
    #产品新增
    def add_product(self):
        url = f"{self.url}/saas/res/product/add?md=057&cmd=043"
        heads = self.headers
        data = {"a": "121",     #a产品名称
                "b": "11-11-1", #产品CAS码
                "c": "454",     #UN码
                "d": 1 ,        #类别
                "e": "7788",    #包装规格
                "f" : "1",      #运输注意事项
                "g":"1",        #应急注意事项
                "h":1 }         # 1吨 ，2车
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    #产品查询
    def detail_product(self,aa):
        url = f"{self.url}/saas/res/product/detail?md=057&cmd=044"
        heads = self.headers
        data = { "aa":aa }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    #产品修改
    def modify_product(self,aa):
        url = f"{self.url}/saas/res/product/modify?md=057&cmd=045"
        heads = self.headers
        data = {"a": "121","aa":aa, "b": "22-21-2","c": "555", "d": 1, "e": "7788", "f": "2", "g": "2"}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res


    #产品删除
    def remove_product(self,aa):
        url = f"{self.url}/saas/res/product/remove?md=057&cmd=046"
        heads = self.headers
        data = {"aa":aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res
class  saas_address(object):

    '''常用地址'''
    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id  = self.saas.login_info(self.user_id)
        self.url     = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                 "user_id": f"{self.user_id}",
                 "product_id": f"{self.product_id}",
                 "cpy_id": f"{self.cpy_id}"
                 }

    #地址新增
    def add_address(self):
        url = f"{self.url}/saas/res/location/add?md=057&cmd=089"
        heads = self.headers
        data = {
            "a": "江苏省-南京市-浦口区",#三级地址
            "b": "江苏省南京市浦口区桥林街道高燕路",#详细地址
            "c": "118.470782,31.974002",#地址坐标
            "d": "名称" ,#地址名称
            "e": "联系单位",#联系单位
            "f" : "联系人",#联系人
            "g":"15037819972",}#手机号码
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    #地址查询
    def detail_address(self,aa):
        url = f"{self.url}/saas/res/location/detail?md=057&cmd=103"
        heads = self.headers
        data = {"aa":aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    #地址删除
    def delete_address(self,aa):
        url = f"{self.url}/saas/res/location/delete?md=057&cmd=090"
        heads = self.headers
        data = {"aa":aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res
class  saas_driver(object):
    '''司机管理'''
    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id  = self.saas.login_info(self.user_id)
        self.url     = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                 "user_id": f"{self.user_id}",
                 "product_id": f"{self.product_id}",
                 "cpy_id": f"{self.cpy_id}"
                 }

    # 司机新增
    def add_driver(self,name,phone,identity):
        url = f"{self.url}/saas/res/driver/add?md=057&cmd=065"
        heads = self.headers
        data = {"a": f"{name}",       #司机姓名
                "b": phone ,          #联系电话
                "c": identity,        #司机身份证号码
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 司机查询
    def detail_driver(self,aa):
        url = f"{self.url}/saas/res/driver/detail?md=057&cmd=066"
        heads = self.headers
        data = {"aa": aa}              #aa主键查询
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 司机修改
    def modify_driver(self, name,phone, identity,aa):
        url = f"{self.url}/saas/res/driver/modify?md=057&cmd=067"
        heads = self.headers
        data = {"a": f"{name}",
                "aa": aa,
                "b":  phone,
                "c":  identity
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 司机删除
    def remove_driver(self,aa):
        url = f"{self.url}/saas/res/driver/remove?md=057&cmd=068"
        heads = self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 司机列表
    def list_driver(self,page,num):
        url = f"{self.url}/saas/res/driver/list?md=057&cmd=064"
        heads = self.headers
        data = {"a":"","b":"","c":"","x":page,"y":num}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res['d'][0]['aa'])
        return res
class  saas_supercargo(object):
    '''押运员管理'''

    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id  = self.saas.login_info(self.user_id)
        self.url = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                 "user_id": f"{self.user_id}",
                 "product_id": f"{self.product_id}",
                 "cpy_id": f"{self.cpy_id}"
                 }

    # 押运员新增
    def add_supercargo(self, name,phone,identity):
        url = f"{self.url}/saas/res/escort/add?md=057&cmd=070"
        heads = self.headers
        data = {"a": f"{name}",     #押运员姓名
                "b": phone,         #押运员联系电话
                "c": identity,      #押运员身份证号码
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 押运员查询
    def detail_supercargo(self,aa):
        url = f"{self.url}/saas/res/escort/detail?md=057&cmd=071"
        heads = self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 押运员修改
    def modify_supercargo(self,name,phone,identity,aa):
        url = f"{self.url}/saas/res/escort/modify?md=057&cmd=072"
        heads = self.headers
        data = {"a": f"{name}",
                "aa": aa,
                "b": phone,
                "c": identity
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 押运员删除
    def remove_supercargo(self,aa):
        url = f"{self.url}/saas/res/escort/remove?md=057&cmd=073"
        heads = self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 押运员列表
    def list_supercargo(self,page,num):
        url = f"{self.url}/saas/res/escort/list?md=057&cmd=069"
        heads = self.headers
        data = {"a":"","b":"","c":"","x":page,"y":num}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res['d'][0]['aa'])
        return res['d'][0]['aa']
class  saas_cars(object):
        '''车辆管理'''

        def __init__(self):
            self.saas = saas1()
            self.user_id = self.saas.user_userid(15137819972, 'e10adc3949ba59abbe56e057f20f883e')
            self.product_id = 2025
            self.cpy_id = self.saas.login_info(self.user_id)
            self.url = "http://180.76.104.7:9538/prod-api"
            self.headers = {"Content-Type": "application/json",
                            "user_id": f"{self.user_id}",
                            "product_id": f"{self.product_id}",
                            "cpy_id": f"{self.cpy_id}"
                            }
        # 车辆新增
        def add_cars(self,car_number):
            url = f"{self.url}/saas/res/car/add?md=057&cmd=075"
            heads = self.headers
            data = {"a": f"{car_number}",
                    "az":[
                          {'a':"carType",'b':"车辆类型","c":""},
                          {'a':"licence", 'b': "道路许可证", "c": ""},
                          {'a': "manageType", 'b': "经营类型", "c": ""}
                          ],
                    "d": "5000",  # 荷载吨数
                    "f": "5000",  # 油耗
                    }
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 车辆查询
        def detail_cars(self,aa):
            url = f"{self.url}/saas/res/car/detail?md=057&cmd=076"
            heads = self.headers
            data = {"aa": aa}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 车辆修改
        def modify_cars(self,car_number,aa):
            url = f"{self.url}/saas/res/car/modify?md=057&cmd=077"
            heads = self.headers
            data = {"aa":aa,#车牌号
                    "a":f"{car_number}",
                    "az":[
                          {'a':"carType",'b':"车辆类型","c":""},
                          {'a':"licence", 'b': "道路许可证", "c": ""},
                          {'a': "manageType", 'b': "经营类型", "c": ""}
                          ],
                    "d": "5100",  # 荷载吨数
                    "f": "5100",  # 油耗
                    }
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 车辆删除
        def remove_cars(self,aa):
            url = f"{self.url}/saas/res/car/remove?md=057&cmd=078"
            heads = self.headers
            data = {"aa": aa}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res

        # 车辆列表
        def list_cars(self, page, num):
            url = f"{self.url}/saas/res/car/list?md=057&cmd=074"
            heads = self.headers
            data = {"a": "", "b": "", "c": "", "x": page, "y": num}
            userproduct = requests.post(url=url, json=data, headers=heads)
            test = userproduct.text
            res = json.loads(test)

            # print(res)
            return res
class  saas_trailer(object):
    '''挂车管理'''

    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972, 'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id = self.saas.login_info(self.user_id)
        self.url = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                        "user_id": f"{self.user_id}",
                        "product_id": f"{self.product_id}",
                        "cpy_id": f"{self.cpy_id}"
                        }

    # 挂车新增
    def add_trailer(self,trailer_number):
        url = f"{self.url}/saas/res/gua/add?md=057&cmd=079"
        heads = self.headers
        data = {"a": f"{trailer_number}",  # 挂车号
                "az": [
                    {'a': "licence", 'b': "道路许可证", "c": ""},
                ],
                "c":"7777",   # 罐体编号
                "d": "5000",  # 荷载吨数
                "e": 1,       # 1上装   2下装
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 挂车查询
    def detail_trailer(self,aa):
        url = f"{self.url}/saas/res/gua/detail?md=057&cmd=081"
        heads = self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 挂车修改
    def modify_trailer(self,trailer_number,aa):
        url = f"{self.url}/saas/res/gua/modify?md=057&cmd=082"
        heads = self.headers
        data = {"aa": aa,
                "a": f'{trailer_number}',# 挂车牌号
                "az": [
                    {'a': "licence", 'b': "道路许可证", "c": ""}
                ],
                "c":"8877",    # 罐体编号
                "d": "51000",  # 荷载吨数
                "e": 2,        # 油耗
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 挂车删除
    def remove_trailer(self,aa):
        url = f"{self.url}/saas/res/gua/remove?md=057&cmd=083"
        heads = self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 挂车列表
    def list_trailer(self,page,num):
        url = f"{self.url}/saas/res/gua/list?md=057&cmd=080"
        heads = self.headers
        data = {"a":"","b":"","c":"","x":page,"y":num}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res
class  saas_transport(object):
    '''运力管理'''

    def __init__(self):
        self.saas = saas1()
        self.user_id = self.saas.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        self.product_id = 2025
        self.cpy_id  = self.saas.login_info(self.user_id)
        self.url = "http://180.76.104.7:9538/prod-api"
        self.headers = {"Content-Type": "application/json",
                 "user_id": f"{self.user_id}",
                 "product_id": f"{self.product_id}",
                 "cpy_id": f"{self.cpy_id}"
                 }

    # 运力新增
    def add_transport(self,b,c,d,e):
        url = f"{self.url}/saas/res/car/driver/add?md=057&cmd=085"
        heads = self.headers
        data = {'a':"运力7",#运力名称
                "b":b,#司机id
                "c":c,#押运员id
                "d":d,#车辆id
                "e":e #挂车id
                }
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res


    # 运力修改
    def modify_trailer(self,aa,b,c,d,e):
        url = f"{self.url}/saas/res/car/driver/modify?md=057&cmd=086"
        heads = self.headers
        data = {'a':"运力7","aa":aa,"b":b,"c":c,"d":d,"e":e}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res

    # 车辆删除
    def remove_trailer(self,aa):
        url = f"{self.url}/saas/res/car/driver/delete?md=057&cmd=087"
        heads =self.headers
        data = {"aa": aa}
        userproduct = requests.post(url=url, json=data, headers=heads)
        test = userproduct.text
        res = json.loads(test)

        # print(res)
        return res


if __name__ == "__main__":
    a = saas_trailer()
    # a.list_trailer(1,10)
    # a.add_cars(car_number(len))
    # a.add_supercargo('韩思雨',19937819972,410203199609111016)
    # a.add_transport()
    # a.add_trailer(428868,2025,15)
    # a.add_driver(428868,2025,15)
    # a.modify_cars(428868,2025,15)
    # a.add_driver(428868,2025,15)
    # a.add_cars(428868,2025,15)
    # a.remove_cars(428868,2025,15)
