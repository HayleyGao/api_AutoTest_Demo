import pytest


# https://www.osgeo.cn/pytest/fixture.html#fixture

# content of test_module.py


def test_hello(hello):
    assert "hello" == hello


def test_(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes


if __name__ == "__main__":
    pytest.main()
