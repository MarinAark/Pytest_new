import pytest


# 写法1️⃣，conftest中的test_usefixture作为参数进行传递
def test_usefixture(usefixture):
    print("这是函数中的usefixture")


# 写法2️⃣，使用标记传递, usefixtures中的参数只能是字符串
@pytest.mark.usefixtures("usefixture")
def test_usefixture2():
    print("这是函数2中的usefixture")


if __name__ == '__main__':
    pytest.main()
