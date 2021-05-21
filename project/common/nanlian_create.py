from common.resouce_center import saas_driver,saas_supercargo,saas_cars,saas_trailer
from faker import Faker
from common.faker_test import car_number,trailer_number

#新增司机10条
# a = saas_driver()
# faker1 = Faker('zh_CN')
# for i in range (1,11):
#     name = faker1.name()
#     phone = faker1.phone_number()
#     identity = faker1.ssn()
#     e = a.add_driver(name,phone,identity)
#     print(e)

#新增押运员10条
# a = saas_supercargo()
# faker1 = Faker('zh_CN')
# for i in range (1,11):
#     name = faker1.name()
#     phone = faker1.phone_number()
#     identity = faker1.ssn()
#     e = a.add_supercargo(name,phone,identity)
#     print(e)

#新增车牌号10条
# a =saas_cars()
# for i in range (1,11):
#     car = car_number(len)
#     e = a.add_cars(car)
#     print(e)
#
# #新增挂车号10条
# a = saas_trailer()
# for i in range (1,11):
#     car = trailer_number(len)
#     e = a.add_trailer(car)
#     print(e)
num_tuple_01 = (1,2,3,4,5)
print(type(num_tuple_01))
print(list(num_tuple_01))
# num_list_01 = list(num_tuple_01)
# print(type(num_list_01))
# print(num_list_01)