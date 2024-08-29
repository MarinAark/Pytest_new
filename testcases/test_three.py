import pytest

@pytest.mark.pro
class Test_Mark:
    def test_one(self):
        expect = 1
        actual = 2
        assert expect != actual

    @pytest.mark.test
    def test_two(self):
        expect = 2
        actual = 2
        assert expect == actual