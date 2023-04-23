import pytest

# https://blog.csdn.net/weixin_46745811/article/details/122384070
# pytest.fixture的两种调用方法：
# 1.作为参数被调用。
# 2.使用usefixtures进行调用。


@pytest.fixture()
def login():
    print("登录成功")
    return "token"


def test_fix(login):
    print(login)


@pytest.mark.usefixtures("login")
def test_two():
    print(login)


def test_three():
    print("test 3")


if __name__ == "__main__":
    pytest.main()


