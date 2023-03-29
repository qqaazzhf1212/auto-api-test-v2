from datetime import datetime
import os
from BeautifulReport import BeautifulReport

from common.HTMLTestRunnerNew import HTMLTestRunner


def report(ts, filename, report_dir, theme='theme_default', title=None, description=None, tester=None, _type=None):
    """
    执行测试用例并且生成报告
    :param ts: 测试套件
    :param filename: 测试报告文件名
    :param report_dir: 测试报告文件夹 仅支持BeautifulReport
    :param theme: 主题  仅支持BeautifulReport
    :param title: 报告标题  仅支持HtmlTestRunner
    :param description:报告描述
    :param tester: 测试人员 仅支持HtmlTestRunner
    :param _type: 默认值为bs，表示生产BeautifulReport的测试报告
    :return:
    """
    theme = theme
    # 1、生成时间前缀
    time_prefix = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # 2、拼接到测试报告文件名
    filename = '{}_{}'.format(time_prefix, filename)
    if _type == 'bs':
        # 生成BeautifulReport的报告
        br = BeautifulReport(ts)
        br.report(description=description, filename=filename, report_dir=report_dir, theme=theme)
    else:
        # 生成HtmlTestRunner的报告
        with open(os.path.join(report_dir, filename), 'wb') as f:
            runner = HTMLTestRunner(f, title=title, description=description, tester=tester)
            runner.run(ts)
