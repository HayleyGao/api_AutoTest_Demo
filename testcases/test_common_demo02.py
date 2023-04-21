from pom import common_demo01
import pytest
import allure


@allure.epic("allure-pytest demo test.")
class TestCommonDemo01:

    @allure.feature("值判断")
    @allure.story('值相等')
    @allure.description(test_description='allure demo01')
    def test_01(self):
        assert common_demo01.func(3) == 4

    @allure.feature("值判断")
    @allure.story("不等")
    def test_02(self):
        assert common_demo01.func(3) != 5

    @allure.feature("值判断")
    @allure.title("小于判断")
    def test_03(self):
        assert common_demo01.func(3) < 5

    @allure.feature("为空判断")
    @allure.title("为空判断")
    @pytest.mark.skip
    def test_04(self):
        assert common_demo01.func(3) is None

    @allure.feature("为空判断")
    @allure.title("不为空判断")
    def test_05(self):
        assert common_demo01.func(3) is not None


if __name__ == "__main__":
    pytest.main(['-sv', __file__])



