import pytest


@pytest.fixture(scope="class", autouse=True)
def login():
    print("登录")
    yield "token：1122334455adminasdddd"
    print("登出")


class TestCase:
    def test_01(self):
        print("test001")

    def test_02(self):
        print("test002")


if __name__ == "__main__":
    pytest.main()

