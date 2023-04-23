import pytest


@pytest.fixture(scope="class", autouse=True)
def login():
    """
    使用fixture实现setup和teardown的用法
    :return:
    """
    print("登录")
    yield "token：1122334455adminasdddd"
    print("登出")


@pytest.fixture(scope="class")
def db_connect():
    print("连接数据库")
    yield
    print("断开数据库连接")


class TestCase:
    def test_01(self):
        print("test001")

    def test_02(self):
        print("test002")


if __name__ == "__main__":
    pytest.main()
