
待安装：
1、安装pytest

2、安装allure
pip3 install allure-pytest

3、requests

# pytest中文文档
https://www.osgeo.cn/pytest/contents.html#full-pytest-documentation

# allure官方文档
https://docs.qameta.io/allure/#_pytest
https://github.com/allure-framework/allure-python


# allure需要设置系统环境变量
#mac 安装allure



# 终端模式下运行命令：
（allure generate 生成测试结果数据 -o 生成报告的路径 --clean）
pytest  ./testcases/test_common_demo02.py   --alluredir ./report/tmp
allure generate ./report/tmp/ -o ./report/html --clean





