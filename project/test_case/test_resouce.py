import unittest
import logging.config
from faker import Faker


logging.config.fileConfig("../config/log.conf")
logging=logging.getLogger()#日志采集器

from common.resouce_center import \
    saas_product,saas_address,saas_client,\
    saas_driver,saas_supercargo,saas_cars,\
    saas_trailer,saas_transport
from common.test import saas1
from common.faker_test import car_number,trailer_number

class client_control(unittest.TestCase):

    """客户管理"""

    @classmethod
    def setUpClass(self):
        self.saas = saas_client()#封装客户管理的类


    @classmethod
    def tearDownClass(cls):
        print('客户管理(增删查)')


        #新增客户
    def test_case1(self):
        global aa
        add = self.saas.add_client()
        aa = add['d']
        self.assertEqual(200,add['a'],msg='客户新增失败')
        logging.info('新增客户')
        # print(aa)
        return aa

        #查询客户
    def test_case2(self):
        query = self.saas.detail_client(aa)
        self.assertEqual(200,query['a'],msg="客户查询失败")
        logging.info('查询客户')


        #修改客户
    def test_case3(self):
        modify = self.saas.modify_client(aa)
        self.assertEqual(1, modify['d'], msg="客户修改失败")  # 1成功  2失败
        logging.info('修改客户')
        #删除客户
    def test_case4(self):
        remove = self.saas.remove_client(aa)
        self.assertEqual(1,remove['d'],msg='客户删除失败')#1成功  2失败
        logging.info('删除客户')
class product_control(unittest.TestCase):

    """产品管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_product()#封装产品管理的类


    @classmethod
    def tearDownClass(cls):
        print('产品管理(增删改查)')


        #新增产品
    def test_case1(self):
        global aa
        add = self.saas.add_product()
        aa = add['d']
        self.assertEqual(200,add['a'],msg='新增产品失败')
        logging.info('新增产品')
        return aa

        #查询产品
    def test_case2(self):
        query = self.saas.detail_product(aa)
        self.assertEqual(200,query['a'],msg="查询产品失败")
        logging.info('查询产品')

        #修改产品
    def test_case3(self):
        modify = self.saas.modify_product(aa)
        self.assertEqual(1,modify['d'],msg="修改产品失败")#1成功  2失败
        logging.info('修改产品')

        #删除产品
    def test_case4(self):
        remove = self.saas.remove_product(aa)
        self.assertEqual(1,remove['d'],msg='删除产品失败')#1成功  2失败
        logging.info('删除产品')
class address_control(unittest.TestCase):

    """地址管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_address()#封装地址管理的类
        self.saas1 = saas1()#公共类获取user_id和cpy_id

        #获取user_id(输入账号和密码)
        self.usr_id =self.saas1.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        #saas产品ID
        self.producct_id = 2025
        #获取cpy_id
        self.cpy_id = self.saas1.login_info(self.usr_id)

    @classmethod
    def tearDownClass(cls):
        print('地址管理(增删查)')


        #新增地址
    def test_case1(self):
        global aa
        add = self.saas.add_address()
        aa = add['d']
        self.assertEqual(200,add['a'],msg='新增地址失败')
        logging.info('新增地址')
        return aa

        #查询地址
    def test_case2(self):
        query = self.saas.detail_address(aa)
        self.assertEqual(200,query['a'],msg="查询地址失败")
        logging.info('查询地址')


        #删除地址
    def test_case3(self):
        remove = self.saas.delete_address(aa)
        self.assertEqual(1,remove['d'],msg='删除地址失败')#1成功  2失败
        logging.info('删除地址')
class driver_control(unittest.TestCase):

    """司机管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_driver()#封装司机管理的类
        self.faker = Faker('zh_CN')
        self.name = self.faker.name()
        self.phone = self.faker.phone_number()
        self.identity = self.faker.ssn()

    @classmethod
    def tearDownClass(cls):
        print('司机管理(增删改查)')


        #新增司机
    def test_case1(self):
        add = self.saas.add_driver(self.name,self.phone,self.identity)
        self.assertEqual(200,add['a'],msg='司机新增失败')
        logging.info('新增司机')

        #司机列表获取新增司机aa主键
    def test_case2(self):
        global aa
        aa = (self.saas.list_driver(1,10))['d'][0]['aa']
        logging.info("司机列表获取aa主键")
        return aa

        #查询司机
    def test_case3(self):
        query = self.saas.detail_driver(aa)
        self.assertEqual(200,query['a'],msg="司机查询失败")
        logging.info('查询司机')

        #修改司机
    def test_case4(self):
        modify = self.saas.modify_driver("张三",19537819972,410203199609111016,aa)
        self.assertEqual(1, modify['d'], msg="司机修改失败")# 1成功  2失败
        logging.info('修改司机')

        #删除司机
    def test_case5(self):
        remove = self.saas.remove_driver(aa)
        self.assertEqual(1,remove['d'],msg='司机删除失败')  #1成功  2失败
        logging.info('删除司机')
class supercargo_control(unittest.TestCase):

    """押运员管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_supercargo()#封装押运员管理的类
        self.faker = Faker('zh_CN')
        self.name  = self.faker.name()#押运员姓名
        self.phone = self.faker.phone_number()#押运员手机号
        self.identity = self.faker.ssn()#押运员身份证号
    @classmethod
    def tearDownClass(cls):
        print('押运员管理(增删改查)')


        #新增押运员
    def test_case1(self):
        add = self.saas.add_supercargo(self.name,self.phone,self.identity)
        self.assertEqual(200,add['a'],msg='押运员新增失败')
        logging.info('新增押运员')

        #押运员列表获取新增押运员aa主键
    def test_case2(self):
        global aa
        aa = self.saas.list_supercargo(1,10)
        logging.info('押运员列表获取押运员aa主键')
        return aa

        #查询押运员
    def test_case3(self):
        query = self.saas.detail_supercargo(aa)
        self.assertEqual(200,query['a'],msg="押运员查询失败")
        logging.info('查询押运员')

        #修改押运员
    def test_case4(self):
        modify = self.saas.modify_supercargo("韩思雨",13037819972,410203199609111016,aa)
        self.assertEqual(1, modify['d'], msg="押运员修改失败")# 1成功  2失败
        logging.info('修改押运员')

        #删除押运员
    def test_case5(self):
        remove = self.saas.remove_supercargo(aa)
        self.assertEqual(1,remove['d'],msg='押运员删除失败')  #1成功  2失败
        logging.info('删除押运员')
class cars_control(unittest.TestCase):

    """车辆管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_cars()#封装车辆管理的类
        self.saas1 = saas1()#公共类获取user_id和cpy_id
        self.car_number = car_number(len)  # 车牌号

        #获取user_id(输入账号和密码)
        self.usr_id =self.saas1.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        #saas产品ID
        self.producct_id = 2025
        #获取cpy_id
        self.cpy_id = self.saas1.login_info(self.usr_id)

    @classmethod
    def tearDownClass(cls):
        print('车辆管理(增删改查)')


        #新增车辆
    def test_case1(self):
        global aa
        add = self.saas.add_cars(self.car_number)
        aa = add['d']
        self.assertEqual(200,add['a'],msg='车辆新增失败')
        logging.info('新增车辆')
        return aa

        #查询车辆
    def test_case2(self):
        query = self.saas.detail_cars(aa)
        self.assertEqual(200,query['a'],msg="车辆查询失败")
        logging.info('查询车辆')

        #修改车辆
    def test_case3(self):
        modify = self.saas.modify_cars(self.car_number,aa)
        self.assertEqual(1, modify['d'], msg="车辆修改失败")# 1成功  2失败
        logging.info('修改车辆')

        #删除车辆
    def test_case4(self):
        remove = self.saas.remove_cars(aa)
        self.assertEqual(1,remove['d'],msg='车辆删除失败')  #1成功  2失败
        logging.info('删除车辆')
class trailer_control(unittest.TestCase):

    """挂车管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_trailer()
        self.saas1 = saas1()#公共类获取user_id和cpy_id
        self.trailer = trailer_number(len) #挂车牌号

        #获取user_id(输入账号和密码)
        self.usr_id =self.saas1.user_userid(15137819972,'e10adc3949ba59abbe56e057f20f883e')
        #saas产品ID
        self.producct_id = 2025
        #获取cpy_id
        self.cpy_id = self.saas1.login_info(self.usr_id)

    @classmethod
    def tearDownClass(cls):
        print('挂车管理(增删改查)')


        #新增挂车
    def test_case1(self):
        global aa
        add = self.saas.add_trailer(self.trailer)
        aa = add['d']
        self.assertEqual(200,add['a'],msg='挂车新增失败')
        logging.info('新增挂车')
        return aa

        #查询挂车
    def test_case2(self):
        query = self.saas.detail_trailer(aa)
        self.assertEqual(200,query['a'],msg="挂车查询失败")
        logging.info('查询挂车')

        #修改挂车
    def test_case3(self):
        modify = self.saas.modify_trailer("京A7788挂" ,aa)
        self.assertEqual(1, modify['d'], msg="挂车修改失败")# 1成功  2失败
        logging.info('修改挂车')

        #删除挂车
    def test_case4(self):
        remove = self.saas.remove_trailer(aa)
        self.assertEqual(1,remove['d'],msg='挂车删除失败') #1成功  2失败
        logging.info('删除挂车')
class transport_control(unittest.TestCase):

    """运力管理"""
    @classmethod
    def setUpClass(self):
        self.saas = saas_transport() #封装挂车管理的类
        self.b    = saas_driver().list_driver(1,10)       #调用司机管理的类
        self.c    = saas_supercargo().list_supercargo(1,10)#调用押运员的类
        self.d    = saas_cars().list_cars(1,10)           #调用车辆管理的类
        self.e    = saas_trailer().list_trailer(1,10)     #封装挂车管理的类


    @classmethod
    def tearDownClass(cls):
        print('运力管理(增删改)')


        #新增运力
    def test_case1(self):
        global aa
        add = self.saas.add_transport(self.b['d'][0]['aa'],self.c['d'][0]['aa'],self.d['d'][0]['aa'],self.e['d'][0]['aa'])
        aa = add['d']
        self.assertEqual(200,add['a'],msg='运力新增失败')
        return aa

        #修改运力
    def test_case2(self):
        modify = self.saas.modify_trailer(aa,self.b['d'][1]['aa'], self.c['d'][1]['aa'], self.d['d'][1]['aa'],self.d['d'][1]['aa'])
        self.assertEqual(1, modify['d'], msg="运力修改失败")# 1成功  2失败

        #删除运力
    def test_case3(self):
        remove = self.saas.remove_trailer(aa)
        self.assertEqual(1,remove['d'],msg='运力删除失败')  #1成功  2失败


if __name__ == "__main__":
    unittest.main()