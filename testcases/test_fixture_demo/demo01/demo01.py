import pytest

# https://www.osgeo.cn/pytest/fixture.html#fixture


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture  # 设置了@pytest.fixture，可以被其它函数，以参数的形式被调用
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket


if __name__ == "__main__":
    pytest.main()
