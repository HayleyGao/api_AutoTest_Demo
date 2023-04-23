import pytest


def add(a, b):
    return a + b


class TestAdd:
    def test_add(self, get_datas, db_connect, login):
        print(get_datas)
        a = get_datas[0]
        b = get_datas[1]
        expect = get_datas[2]
        assert expect == add(a, b)


if __name__ == "__main__":
    pytest.main()
