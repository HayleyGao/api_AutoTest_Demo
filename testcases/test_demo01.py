import pytest


def func(x):
    return x + 1


def test_answer_01():
    assert func(3) == 4


def test_answer_02():
    assert func(3) != 5


if __name__ == "__main__":
    pytest.main()

