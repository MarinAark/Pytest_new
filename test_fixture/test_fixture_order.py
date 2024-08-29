import pytest


@pytest.fixture(scope="session")
def t_session():
    print("这是一个session fixture")


@pytest.fixture(scope="function")
def t_function():
    print("这是一个function fixture")


@pytest.fixture(scope="module")
def t_module():
    print("这是一个module fixture")


@pytest.fixture(scope="class")
def t_class():
    print("这是一个class fixture")


class TestOrder:
    def test_order(self, t_class, t_module, t_session, t_function):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()