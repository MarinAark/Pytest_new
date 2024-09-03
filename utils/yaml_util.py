import random
from faker import Faker

faker = Faker(locale="zh-CN")

def func_yaml(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if '${' and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start + 2:end]
                # 使用 eval 执行占位符中的函数，并将结果替换
                data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:]
    return data

def random_name():
    return faker.name()

def age():
    return random.randint(20, 80)

if __name__ == '__main__':
    data = {"name": "杭州-${random_name()}-测试开发工程师", "age": "${age()}", "gender": "boy"}
    print(func_yaml(data))
