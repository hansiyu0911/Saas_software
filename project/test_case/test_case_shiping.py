import unittest
import requests
from common.test import saas1
import re
import logging.config



# 匹配日志文件
# 采集器
# logging.config.fileConfig("../config/log.conf")()
# logging=logging.getLogger

class shiping(unittest.TestCase):
    # saas = saas1()
    @classmethod
    def setUpClass(cls):
      cls.b = saas1()


    def test01(self):

        #发布货单
        dingdan = self.b.release_mainfest(428868,2025,15)
        self.assertEqual(200, dingdan['a'], msg='发布货单失败')
        print(dingdan)
        dingdan1 = re.findall("货单编号.(.*)?", dingdan["m"])

        #数据库删除货单
        self.b.MySqL(dingdan1[0])
        print(dingdan1)


    def test02(self):

        pass




















    # def test01(self):
    #     #获取客户信息
    #     result = self.b.user_client(428781,2025,15)
    #     b = result['d'][0]['aa']# 客户ID
    #     c = result['d'][0]['a'] # 客户名称
    #     d = result['d'][0]['c'] # 联系人
    #     e = result['d'][0]['d'] # 联系电话
    #
    #     #获取产品信息
    #     result1 = self.b.user_product(428781,2025,15)
    #     f = result1['d'][0]['aa'] # 产品ID
    #     g = result1['d'][0]['a']  # 产品名称
    #
    #
    #     #装卸货地址
    #     result2 = self.b.user_coordinate(428781,2025,15)
    #     dizhi_a = result2["d"][0]["aa"]
    #     dizhi_b = result2["d"][0]["d"]
    #     dizhi_e = result2["d"][0]["a"]
    #     dizhi_f = result2["d"][0]["b"]
    #     dizhi_g = result2["d"][0]["c"]
    #
    #     dingdan = self.b.release_mainfest(428781,2025,15,)






if __name__ == "__main__":
    unittest.main()