import pymysql
from sshtunnel import SSHTunnelForwarder
from common.test import saas1
import time
# print(release_mainfest())
with SSHTunnelForwarder(
         ('180.76.104.7' , 22),
         ssh_password='Wcgj2018*',
         ssh_username='root',
         remote_bind_address=('192.168.0.10' ,  3306)) as server:

    conn = pymysql.connect(host='127.0.0.1',              #本机host
                           port=server.local_bind_port,
                           user='root',
                           passwd='123456',
                           charset = 'utf8',)
    # print(conn)
    cur = conn.cursor()
    # cur.execute('show databases')
    cur.execute('use ftc_saas')
    time.sleep(2)
    cur.execute(f"delete from t_t_goods_order where order_serial='{saas1.release_mainfest}'")
    conn.commit()
    print('删除成功')
    # a = cur.fetchall()
    # cur.execute(f"delete from t_t_goods_order where order_serial='{release_mainfest()}'")
