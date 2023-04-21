import pytest


class TestDemo02:

    def test_01(self):
        x = 'this'
        assert "h" in x

    def test_02(self):
        x = "hello"
        assert hasattr(x, "e")


if __name__ == "__main__":
    pytest.main()
