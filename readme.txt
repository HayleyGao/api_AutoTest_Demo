
一、安装需要的第三方库
1、安装pytest
pip3 install pytest

2、安装allure
pip3 install allure-pytest

3、requests

pytest中文文档
https://www.osgeo.cn/pytest/contents.html#full-pytest-documentation
pytest文档
https://docs.pytest.org/en/6.2.x/contents.html

allure官方文档
https://docs.qameta.io/allure/#_pytest
https://github.com/allure-framework/allure-python

allure需要设置系统环境变量
mac下载安装allure，配置环境变量


二、生成报告

方式一：allure-pytest
终端模式下运行命令：
（allure generate 生成测试结果数据 -o 生成报告的路径 --clean）
pytest  ./testcases/test_common_demo02.py   --alluredir ./report/tmp
allure generate ./report/tmp/ -o ./report/html --clean



方式二：pytest-html插件
(pytest插件 pytest-html插件)
pip3 install pytest-html

main.py
pytest.main(['./testcases/test_common_demo03.py', "--html=./report/result/report.html"])

( pytest-html插件 生成的html格式的报告更简单清晰一些)

https://pytest-html.readthedocs.io/en/latest/



