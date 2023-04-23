import pytest
import yaml

# https://blog.csdn.net/weixin_46745811/article/details/122384070


@pytest.fixture(scope="class")
def login():
    """
    使用fixture实现setup和teardown的用法
    :return:
    """
    print("登录")
    yield
    print("登出")


@pytest.fixture(scope="class")
def db_connect():
    print("连接数据库")
    yield
    print("断开数据库连接")


def get_yaml():
    with open("./add_data.yaml") as f:
        # 使用yaml解析文件流，生成一个python可识别的数据类型
        data = yaml.safe_load(f)
        print(data)
    return data


@pytest.fixture(params=get_yaml()["data"], ids=get_yaml()["ids"])
def get_datas(request):
    data = request.param
    return data


if __name__ == "__main__":
    pytest.main()
