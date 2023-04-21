import pytest

if __name__ == '__main__':
    # pytest.main(['-v'])
    pytest.main(['./testcases/test_common_demo03.py', "--html=./report/result/report.html"])
