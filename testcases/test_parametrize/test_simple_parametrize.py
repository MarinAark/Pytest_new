import pytest

# @pytest.mark.parametrize("name", ["麦琪"])
# def test_parametrize(name):
#     print(f'this is {name}')
# 单个参数
expects_name = ["赵云", "刘备", "关于", "张飞", "马超"]


@pytest.mark.parametrize("name", expects_name)
def test_parametrize(name):
    assert name in expects_name
