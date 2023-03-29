import unittest

from conf import settings
from common.handler_reports import report

if __name__ == '__main__':
    # 收集测试用例
    ts = unittest.TestLoader().discover('test_cases/')
    report(ts, **settings.API_REPORT_CONFIG)

    # 运行器运行生成报告
    # 1、HTMLTestRunner
    # with open('reports/apitest测试报告.html', 'wb') as f:
    #     runner = HTMLTestRunner(stream=f, title='api测试报告', description='api测试报告', tester='LH')
    #     runner.run(ts)

    # 2、BeautifulReport
    # br = BeautifulReport(ts)
    # br.report(description='api测试报告', filename='./results/reports/apitest测试报告.html')
    # br.report(**settings_api.REPORT_CONFIG)
