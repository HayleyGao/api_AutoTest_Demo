import pytest
from utils import logger

# log = logger.Log(__name__).getlog()


# 当文档使用的参考，直观
# https://blog.csdn.net/weixin_44809381/article/details/118438911

# https://blog.csdn.net/weixin_46745811/article/details/122384070


if __name__ == '__main__':
    # pytest.main(['-v'])
    log = logger.Log(__name__).getlog()
    log.info("I am main.py")
    pytest.main(['./testcases/test_common_demo03.py', "--html=./report/result/report.html"])

