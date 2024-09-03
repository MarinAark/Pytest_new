import pytest
import yaml
import os
import configparser

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "settings.ini")


class readFiles:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path


    def read_data(self):
        # 1. 调用，打开并读取YAML文件
        f = open(self.data_path, mode="r", encoding="utf-8")
        data = yaml.safe_load(f)
        return data


    def read_ini(self):
        # 2. 调用，打开并读取INI文件
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding="utf-8")
        return config


# 创建readFiles类的实例
base_data = readFiles()


