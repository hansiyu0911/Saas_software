from faker import Faker
fake = Faker('zh_CN')#切换简体中文
print(fake.name())#生成中文名字
# print(fake.address())#生成地址
print(fake.company())#生成公司
# print(fake.latitude())#维度
# print(fake.longitude())#经度
print(fake.phone_number())#手机号码
# print(fake.ssn())#身份证号
# print(fake.province())#省份
# print(fake.city_name())#城市

# print(1,2,3,sep="\n")

import random
def car_number(len):
  char0='京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
  char1='ABCDEFGHJKLMNPQRSTUVWXYZ'#车牌号中没有I和O，可自行百度
  char2='1234567890'
  len0=  len(char0) - 1
  len1 = len(char1) - 1
  len2 = len(char2) - 1
  while True:
    code = ''
    index0 = random.randint(1,len0 )
    index1 = random.randint(1, len1)
    code += char0[index0]
    code += char1[index1]
    for i in range(1, 6):
      index2 = random.randint(1, len2)
      code += char2[index2]
    # print(code)
    return code

def trailer_number(len):
  char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
  char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，可自行百度
  char2 = '1234567890'
  len0 = len(char0) - 1
  len1 = len(char1) - 1
  len2 = len(char2) - 1
  while True:
      trailer_code = ''
      index0 = random.randint(1, len0)
      index1 = random.randint(1, len1)
      trailer_code += char0[index0]
      trailer_code += char1[index1]
      for i in range(1, 5):
          index2 = random.randint(1, len2)
          trailer_code += char2[index2]
      code = trailer_code + "挂"
      # print(code)
      return code





if __name__=='__main__':
    car_number(len)
    trailer_number(len)