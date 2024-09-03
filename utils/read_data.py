import yaml
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "data.yaml")
def read_data():
    # 1. 调用config.yaml文件
    f = open(path, mode="r", encoding="utf-8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()
print(get_data)
print(get_data["person"])
# print(get_data["test"])
# print(get_data["test"]["name"])
# print(get_data["test"]["request"])
# print(get_data["test"]["request"]["url"])
# print(get_data["test"]["request"]["method"])
# print(get_data["test"]["request"]["headers"])
# print(get_data["test"]["request"]["headers"]["Content-Type"])
# print(get_data["test"]["request"]["json"])
# print(get_data["test"]["request"]["json"]["username"])
# print(get_data["test"]["request"]["json"]["password"])

# print("===========打印hero字典===========")
# print(data["hero"])
# print("\n")
#
# print("===========打印heroes1字典===========")
# print(data["heroes1"])
# print("\n")
#
# print("===========打印hero_name字典===========")
# print(data["hero_name"])
# print("\n")
#
# print("===========打印heroes字典===========")
# print(data["heroes"])
# print("\n")
#
# print("===========打印color_name字典===========")
# print(data["color_name"])
