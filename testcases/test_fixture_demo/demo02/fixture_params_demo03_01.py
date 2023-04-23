import pytest

# 测试数据的传递，通过参数进行传递。
# fixture 通过固定参数 request 传递
"""
fixture实现参数化
"""


@pytest.fixture(params=['tom', 'jack', 'lily'], ids=["name1", "name2", "name3"])
def demo01(request):
    print("登录")
    yield request.param
    print("登出")


def test_demo(demo01):
    print("用户名", demo01)


if __name__ == "__main__":
    pytest.main()
