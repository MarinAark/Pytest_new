import pytest

class Test_eshop_login:
    @pytest.mark.run(order=1)
    def test_login(self):
        print("login....")

    @pytest.mark.run(order=3)
    def test_order(self):
        print("ordering")

    @pytest.mark.run(order=2)
    def test_search(self):
        print("searching")

    @pytest.mark.run(order=4)
    def test_pay(self):
        print("paying")
