import pytest


class TestCase:
    def test_01(self,login,db_connect):
        print("test001")

    def test_02(self,login,db_connect):
        print("test002")


if __name__ == "__main__":
    pytest.main()

