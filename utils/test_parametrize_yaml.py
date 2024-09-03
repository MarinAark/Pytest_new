import pytest
import yaml
# 引入utils 文件夹下面的 read_data.py
from utils.read_data import get_data
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "data.yaml")
# 2.引入read_data文件，并获取get_data中的hero，进行测试用例的判断


@pytest.mark.parametrize("name, word", get_data["heroes_and_words"])
def test_parametrize_02(name, word):
    print(f"{name}'s word is {word}")

