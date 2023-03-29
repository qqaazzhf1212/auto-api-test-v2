import json
import unittest

from jsonpath import jsonpath
import requests
from conf import settings
from common import logger, db
from common.handler_test_data import replace_args, gencreate_phone
from common.handler_make_requests import send_http_requests


class BaseTest(unittest.TestCase):
    name = 'base用例'  # 这个属性应该被覆盖
    logger = logger
    db = db
    settings = settings

    # 会画对象
    session = requests.session()

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.debug('======={}接口开始测试======'.format(cls.name))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.debug('======={}接口测试结束======'.format(cls.name))

    def checkout(self, case):
        self.logger.debug('======用例【{}: {}】开始测试======'.format(case['id'], case['title']))
        # 绑定对应，方便测试数据处理
        self.case = case
        # 1、测试数据处理
        self.pre_test_data()
        # 2、测试步骤
        self.setp()
        # 3、响应状态码断言
        self.assert_staus_code()
        # 4、响应数据断言
        self.assert_json_response()
        # 5、数据库断言
        self.assert_db_true()
        # 6、提取数据
        self.extract_data()
        self.logger.debug('======用例【{}】测试结束======'.format(self.case['title']))

    def pre_test_data(self):
        '''
        预处理数据
        :return:
        '''

        # 替换数据
        self.case['requests'] = replace_args(self.case['requests'], self)

        # 替换sql
        if self.case['check_sql']:
            self.case['check_sql'] = replace_args(self.case['check_sql'], self)

        # 判断是否生成手机号
        if '#phone#' in self.case['requests']:
            phone = gencreate_phone()
            # 替换槽位
            self.case['requests'] = self.case['requests'].replace('#phone#', phone)
            # 替换sql
            if self.case['check_sql']:
                self.case['check_sql'] = self.case['check_sql'].replace('#phone#', phone)

        # 将json字段串转换为python对象
        try:
            self.case['requests'] = json.loads(self.case['requests'])
            self.case['expected'] = json.loads(self.case['expected'])
        except Exception as e:
            self.logger.exception('用例【{}】的json的格式不正确'.format(self.case['title']))
            self.logger.exception('case["requests"]:{}'.format(self.case['requests']))
            self.logger.exception('case["expected"]:{}'.format(self.case['expected']))
            raise ValueError('用例【{}】的json的格式不正确'.format(self.case['title']))

        # 拼接url
        if self.case['url'].startswith('http') or self.case['url'].startswith("https://"):
            self.case['url'] = self.case['url']
        else:
            self.case['url'] = settings.API_PROJECT_HOST + settings.API_INTERFACE[self.case['url']]

    def setp(self):
        self.logger.debug('用例的【{}】的请求url：{}'.format(self.case['title'], self.case['url']))
        self.logger.debug('用例的【{}】的请求method：{}'.format(self.case['title'], self.case['method']))
        self.logger.debug('用例的【{}】的请求args：{}'.format(self.case['title'], self.case['requests']))
        '''
        测试步骤
        :return:
        '''
        try:
            self.response = send_http_requests(url=self.case['url'], method=self.case['method'],
                                               **self.case['requests'])
            self.logger.debug('用例【{}】返回结果：{}'.format(self.case['title'], self.response.json()))
        except Exception as e:
            self.logger.exception('用例【{}】发送请求http错误'.format(self.case['title']))
            self.logger.debug('用例url：{}'.format(self.case['url']))
            self.logger.debug('用例method：{}'.format(self.case['method']))
            self.logger.debug('用例args：{}'.format(self.case['requests']))
            raise e

    def assert_staus_code(self):
        '''
        响应状态码断言
        :return:
        '''
        self.logger.debug('用例【{}】请求状态码断言：{}'.format(self.case['title'], self.case['status_code']))
        code = self.case['status_code']
        try:
            self.assertEqual(code, self.response.status_code)
        except AssertionError as e:
            self.logger.exception('用例【{}】请求状态码断言失败'.format(self.case['title']))
            raise e
        else:
            self.logger.debug('用例【{}】请求状态码断言成功'.format(self.case['title']))

    def assert_json_response(self):
        '''
        响应数据断言
        :return:
        '''
        # 处理excel的预期结果
        self.logger.debug('用例【{}】请求结果断言：{}'.format(self.case['title'], self.case['expected']))
        old_keys = []
        new_keys = []
        except_keys = []
        values = []

        except_data = {}
        response_data = {}
        try:
            for key, value in self.case['expected'].items():
                # self.logger.debug('用例【{}】获取key和value成功，key：{}，value：{}'.format(self.case['title'], key, value))
                old_keys.append(key)
                values.append(value)
            for key in old_keys:
                key = key.split(':')
                new_keys.append(key[0])
                except_keys.append(key[1])
            except_data = dict(zip(new_keys, values))
            response_data = dict(zip(except_keys, values))
            # self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], old_keys))
            # self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], new_keys))
            # self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], except_keys))
            # self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], values))
            self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], except_data))
            self.logger.debug('用例【{}】的预期结果{}'.format(self.case['title'], response_data))
        except AssertionError as e:
            self.logger.exception('用例【{}】获取key和value失败'.format(self.case['title']))
            raise e

        # 断言判断
        # res_data = self.response.json()
        response = self.response.json()
        res_data = {}
        jsonpath_ex = []
        for ex in response_data:
            # print(ex)
            res = jsonpath(self.response.json(), ex)[0]
            jsonpath_ex.append(res)
        # print(jsonpath_ex)
        res_data = dict(zip(new_keys, jsonpath_ex))
        # print(res_data)

        try:
            # self.assertEqual(self.case['expected'], res)
            self.assertEqual(res_data, except_data)
        except AssertionError as e:
            self.logger.exception('用例【{}】请求结果断言失败'.format(self.case['title']))
            self.logger.debug('用例【{}】的期望数据：{}'.format(self.case['title'],self.case['expected']))
            self.logger.debug('用例【{}】的实际结果是：{}'.format(self.case['title'],response))
            self.logger.debug('用例【{}】的响应结果是：{}'.format(self.case['title'],res_data))
            raise e
        else:
            self.logger.debug('用例【{}】的期望数据：{}'.format(self.case['title'], except_data))
            self.logger.debug('用例【{}】的实际结果是：{}'.format(self.case['title'], response))
            self.logger.debug('用例【{}】的响应结果是：{}'.format(self.case['title'], res_data))
            self.logger.debug('用例【{}】请求结果断言成功'.format(self.case['title']))

    def assert_db_true(self):
        '''
        数据库断言
        :return:
        '''
        if self.case['check_sql']:
            try:
                db_res = self.db.exist(self.case['check_sql'])
                self.assertTrue(db_res)
            except Exception as e:
                self.logger.exception('用例【{}】数据库断言失败'.format(self.case['title']))
                self.logger.debug('执行的sql是：{}'.format(self.case['check_sql']))
                raise e
            else:
                self.logger.debug('用例【{}】数据库断言成功'.format(self.case['title']))

    def extract_data(self):
        '''
        提取响应的数据
        :return:
        '''
        if self.case['extract']:
            try:
                exps = json.loads(self.case['extract'])
                self.logger.debug('用例【{}】提取数据{}成功'.format(self.case['title'], self.case['extract']))
            except Exception as e:
                raise ValueError('用例【{}】的extract提取表达式不正确'.format(self.case['title']))

            for item in exps:
                # print(item)
                name = item['name']
                exp = item['exp']
                # print(exp)
                res = jsonpath(self.response.json(), exp)
                # print(res)

                if res:
                    # 保存到类的属性
                    setattr(self.__class__, name, res[0])
                else:
                    raise ValueError('用例【{}】的extract提取表达式不正确:{}'.format(self.case['title'], exp))

    # def send_http_requests(self, url, method, **kwargs) -> requests.Response:
    #     '''发送http请求'''
    #     # 把方法名小写话
    #     method = method.lower()
    #     # 获取对应的方法
    #     return getattr(self.session, method)(url=url, **kwargs)
