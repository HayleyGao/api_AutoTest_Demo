# contents of test_append.py
import pytest

# 测试/夹具可以 请求 一次安装多个固定装置（可以设置多个参数进行使用的意思。）

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def second_entry():
    return 2


# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list


if __name__ == "__main__":
    pytest.main()
