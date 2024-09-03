import pytest

name_and_word_1 = [["关羽", "茶婊买手"], ["张飞", "俺也一样"]]  # value 为列表格式
name_and_word_2 = [("关羽", "茶婊买手"), ("张飞", "俺也一样")]  # value 为集合格式
name_and_word_3 = [{"name": "关羽", "word": "茶婊买手"}, {"name": "张飞", "word": "俺也一样"}]  # value 为字典格式
name_and_word_4 = {
    "关羽": "茶婊买手",
    "张飞": "俺也一样"
}


# @pytest.mark.parametrize("name, word", name_and_word_1)
@pytest.mark.parametrize("name, word", name_and_word_2)
def test_verify_parametrize(name, word):
    print(f"{name} :{word}")
    assert "关羽" in name or "张飞" in name


@pytest.mark.parametrize("data", name_and_word_3)
def test_verify_parametrize_2(data):
    name = (data["name"])
    word = (data["word"])
    print(f'{name}:{word}')
    assert "关羽" in name or "张飞" in name


@pytest.mark.parametrize("name", name_and_word_4)
def test_verify_parametrize_3(name):
    word = name_and_word_4[name]
    print(f'{name}:{word}')
    assert "关羽" in name or "张飞" in name