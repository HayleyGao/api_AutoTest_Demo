import pytest
from utils import logger

log = logger.Log(__name__).getlog()


if __name__ == '__main__':
    # pytest.main(['-v'])
    log.info("I am main.py")
    pytest.main(['./testcases/test_common_demo03.py', "--html=./report/result/report.html"])
