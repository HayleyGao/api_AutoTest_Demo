from pom import common_demo01
import pytest


class TestCommonDemo01:
    def test_01(self):
        assert common_demo01.func(3) == 4

    def test_02(self):
        assert common_demo01.func(3) != 5

    @pytest.mark.xfail  # 将测试功能标记为预期失败
    def test_03(self):
        assert common_demo01.func(3) == 5


if __name__ == "__main__":
    pytest.main()
    # pytest. / testcases / test_common_demo03.py --html =./report/result/report.html
