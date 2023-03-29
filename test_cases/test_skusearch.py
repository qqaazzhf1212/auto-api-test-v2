import json
from unittest.mock import create_autospec

from test_cases.base_case import BaseTest
from conf import settings
from common.myddt import ddt, data
from common.api_fixture import login
from common.handler_test_data import get_test_data_from_excel

sheet_name = '搜索'
cases = get_test_data_from_excel(file=settings.API_TEST_DATA_FILE, sheet_name=sheet_name)


@ddt
class SkuSearch(BaseTest):
    name = '搜索'

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('=======搜索接口开始测试======')
        username = settings.API_LOGIN_TEST['username']
        password = settings.API_LOGIN_TEST['password']
        data = login(username=username, password=password)
        # print(data)
        if data is None:
            cls.logger.error('{}账号，登录失败'.format(username))
            raise ValueError('{}账号，登录失败'.format(username))
        cls.logger.error('{}账号，登录成功'.format(username))
        cls.user_id = data['user']['user']['id']
        cls.token = data['token']


    @data(*cases)
    def test_skusearch(self, case):
        self.checkout(case)
        # self.logger.info('用例【{}: {}】开始测试'.format(case['id'], case['title']))
        # # 替换槽位
        # replace_args(case['requests'], self)
        #
        # case['requests'] = case['requests'].replace('#token#', self.token)
        # case['requests'] = json.loads(case['requests'])
        # case['expected'] = json.loads(case['expected'])
        #
        # case['url'] = settings.PROJECT_HOST + settings.INTERFACE[case['url']]
        #
        # self.logger.info('用例的url：{}'.format(case['url']))
        # self.logger.info('用例的method：{}'.format(case['method']))
        # self.logger.info('用例的args：{}'.format(case['requests']))
        # response = send_http_requests(url=case['url'], method=case['method'], **case['requests'])
        # response_data = response.json()
        #
        # # 1、状态码断言
        # self.logger.info('状态码断言：{}'.format(case['status_code']))
        # code=case['status_code']
        # try:
        #     self.assertEqual(code, response.status_code)
        # except AssertionError as e:
        #     self.logger.exception('状态码断言失败')
        #     raise e
        # else:
        #     self.logger.info('状态码断言成功')
        #
        # # 2、请求结果断言
        # res = {'code': response.status_code}
        # try:
        #     self.assertEqual(case['expected'], res)
        # except AssertionError as e:
        #     self.logger.exception('请求结果断言失败')
        #     self.logger.debug('期望数据：{}'.format(case['expected']))
        #     self.logger.debug('实际结果是：{}'.format(res))
        #     self.logger.debug('响应结果是：{}'.format(response_data))
        #     raise e
        # else:
        #     self.logger.info('请求结果断言成功')
        #
        # # 3、校验数据库
        # # print(case['check_sql'])
        # if case['check_sql']:
        #     try:
        #         db_res = self.db.exist(case['check_sql'])
        #         self.assertTrue(db_res)
        #     except Exception as e:
        #         self.logger.exception('数据库断言失败')
        #         self.logger.debug('执行的sql是：{}'.format(case['check_sql']))
        #         raise e
        #     else:
        #         self.logger.info('数据库断言成功')
        #
        # self.logger.info('用例【{}】测试结束'.format(case['title']))

        def setp(self):
            super().setp()

        def assert_db_true(self):
            '''
            多条sql验证
            :return:
            '''
            if self.case['check_sql']:
                sqls = json.loads(self.case['check_sql'])
                for sql in sqls:
                    try:
                        db_res = self.db.exist(sql)
                        self.assertTrue(db_res)
                    except Exception as e:
                        self.logger.exception('用例【{}】数据库断言失败'.format(self.case['title']))
                        self.logger.debug('执行的sql是：{}'.format(sql))
                        raise e

                self.logger.debug('用例【{}】数据库断言成功'.format(self.case['title']))

        def setp(self):
            a_url = 'http://www.aaa.com'
            # 自定义返回数据
            a_mock = create_autospec(self.send_http_requests, return_value='成功')
            # 执行mock方法
            pay_res = a_mock(a_url, method=self.case['method'], **self.case['requests'])

            super().setp()
            print(pay_res)

if __name__ == '__main__':
    SkuSearch()
