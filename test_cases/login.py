from conf import settings
from common.myddt import data, ddt
from common.handler_test_data import get_test_data_from_excel

from test_cases.base_case import BaseTest

sheet_name = '登陆'
cases = get_test_data_from_excel(file=settings.API_TEST_DATA_FILE, sheet_name=sheet_name)


@ddt
class Register(BaseTest):
    name = '登录'

    @data(*cases)
    def test_register(self, case):
        self.checkout(case)
    #     self.logger.info('用例【{}: {}】开始测试'.format(case['id'], case['title']))
    #     # 数据处理
    #     if '#phone#' in case['requests']:
    #         phone = gencreate_phone()
    #         # 替换槽位
    #         case['requests'] = case['requests'].replace('#phone#', phone)
    #         # 替换sql
    #         if case['check_sql']:
    #             case['check_sql'] = case['check_sql'].replace('#phone#', phone)
    #
    #     case['requests'] = json.loads(case['requests'])
    #     case['expected'] = json.loads(case['expected'])
    #     print(case['requests'], type(case['requests']))
    #     print(case['requests'], type(case['requests']))
    #     # case['check_sql'] = json.loads(case['check_sql'])
    #     # print(settings.REPORT_CONFIG)
    #     # print(settings.INTERFACE[case['url']])
    #     case['url'] = settings.PROJECT_HOST + settings.INTERFACE[case['url']]
    #
    #     self.logger.info('用例的url：{}'.format(case['url']))
    #     self.logger.info('用例的method：{}'.format(case['method']))
    #     self.logger.info('用例的args：{}'.format(case['requests']))
    #     # print(case['requests'],type(case['requests']))
    #     response = send_http_requests(url=case['url'], method=case['method'], **case['requests'])
    #     # print(response)
    #     response_data = response.json()
    #     # print(response_data)
    #     # print(case['expected'])
    #
    #     # 1、状态码断言
    #     try:
    #         self.assertEqual(200, response.status_code)
    #     except AssertionError as e:
    #         self.logger.exception('状态码断言失败')
    #         raise e
    #     else:
    #         self.logger.info('状态码断言成功')
    #
    #     # 2、请求结果断言
    #     res = {'code': response.status_code}
    #     try:
    #         self.assertEqual(case['expected'], res)
    #     except AssertionError as e:
    #         self.logger.exception('请求结果断言失败')
    #         self.logger.debug('期望数据：{}'.format(case['expected']))
    #         self.logger.debug('实际结果是：{}'.format(res))
    #         self.logger.debug('响应结果是：{}'.format(response_data))
    #         raise e
    #     else:
    #         self.logger.info('请求结果断言成功')
    #
    #     # 3、校验数据库
    #     # print(case['check_sql'])
    #     if case['check_sql']:
    #         try:
    #             db_res = self.db.exist(case['check_sql'])
    #             self.assertTrue(db_res)
    #         except Exception as e:
    #             self.logger.exception('数据库断言失败')
    #             self.logger.debug('执行的sql是：{}'.format(case['check_sql']))
    #             raise e
    #         else:
    #             self.logger.info('数据库断言成功')
    #
    #     self.logger.info('用例【{}】测试结束'.format(case['title']))


if __name__ == '__main__':
    Register()
