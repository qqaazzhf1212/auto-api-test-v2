import os

# 根项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# repost目录
API_REPORT_DIR = os.path.join(BASE_DIR, 'results/reports/')

# log目录
API_LOG_DIR = os.path.join(BASE_DIR, 'results/logs/api.log')

# 测试用例路径
API_CASES_DIR = os.path.join(BASE_DIR, 'test_datas/api_cases.xlsx')


# 数据库配置
# 本地DB
# DB_CONFIG = {
#     "host": '127.0.0.1',
#     "user": 'root',
#     "password": '123456',
#     "db": 'autotest',
#     "charset": 'utf8',
#     "port": 3306,
#     'autocommit': True  # 自动提交事务，防止重复读的问题
# }
DB_CONFIG = {
    "host": 'XXXX',
    "user": 'XXXX',
    "password": 'XXX',
    "db": 'XXXX',
    "charset": 'utf8',
    "port": XXX,
    'autocommit': True  # 自动提交事务，防止重复读的问题
}

# ===============================api======================================


# 项目配置
API_PROJECT_HOST = 'XXXX'

# 接口地址
API_INTERFACE = {
    'login': '/auth/login',
    'sku_search': '/product/sku/page',
    'medicalmanage': '/product/sku/pagedListHealthCare'
}

API_LOGIN_TEST = {
    'username': 'admin',
    'password': 'XXXXX'
}

# 日志配置
API_LOG_CONFIG = {
    "name": "api",
    "filename": API_LOG_DIR,
    "debug": True,
}

# 测试数据配置
API_TEST_DATA_FILE = API_CASES_DIR

# 测试报告配置
API_REPORT_CONFIG = {
    "filename": 'api测试报告.html',
    "description": "api测试报告",
    'report_dir': API_REPORT_DIR,
    'title': 'api测试报告',
    'theme': 'theme_memories',
    '_type': 'bs'
}

