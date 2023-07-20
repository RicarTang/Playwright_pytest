"""公共配置"""
import os

# 项目根目录
ROOT_PATH = os.path.dirname(__file__)
# 目标url
TEST_URL = "http://127.0.0.1:6939"
# pytest report目录
REPORT_DATA = os.path.join(ROOT_PATH,'report_data')
# allure报告目录
ALLURE_REPORT = os.path.join(ROOT_PATH,'allure_report')

# 日志级别
STREAM_LOG_LEVEL = "DEBUG"
FILE_LOG_LEVEL = "INFO"
# 日志格式
LOG_FORMATTER = "%(levelname)s:     %(asctime)s - %(filename)s - %(funcName)s - line: %(lineno)d - message: %(message)s"

# data数据文件目录
# 测试用例数据
TESTCASE_DATA_PATH = os.path.join(ROOT_PATH,'data','test_data')