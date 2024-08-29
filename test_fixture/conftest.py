import pytest


@pytest.fixture(scope="session")
def test_session():
    print("提前了，这是session级别的fixtrue")


@pytest.fixture(scope="function")
def test_func():
    print("这是func级别的fixture")


@pytest.fixture(scope="function")
def test_func2():
    print("这是func2级别的fixture")


@pytest.fixture(scope="function")
def get_params():
    params = {
        "shouji": "13456755448",
        "appkey": "0c818521d38759e1"
    }
    return params


@pytest.fixture(scope="function", autouse=True)
def fun():
    print("这是fixture的前置步骤")
    yield
    print("这是fixture的后置步骤")

@pytest.fixture(scope="function")
def usefixture():
    print("这是conftest里面的usefixture")