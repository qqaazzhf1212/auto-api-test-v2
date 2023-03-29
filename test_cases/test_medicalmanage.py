from common.myddt import ddt, data
from test_cases.base_case import BaseTest
from jsonpath import jsonpath
from common.api_fixture import login

from common.handler_test_data import get_test_data_from_excel

sheet_name = '医保数据管理'
cases = get_test_data_from_excel(file=BaseTest.settings.API_TEST_DATA_FILE, sheet_name=sheet_name)


@ddt
class TestMedManage(BaseTest):
    name = '医保数据管理'

    @data(*cases)
    def test_medicalmanage_search(self, case):
        self.checkout(case)

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('=======医保数据管理获取token开始测试======')
        cls.token = jsonpath(login(BaseTest.settings.API_LOGIN_TEST['username'], BaseTest.settings.API_LOGIN_TEST['password']),"$..token")[0]
        # print(cls.token)
        cls.logger.info('=======医保数据管理获取token成功==========')
