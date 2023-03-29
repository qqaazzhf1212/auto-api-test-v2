from .handler_log import get_logger
from conf import settings
from .handler_db import DB

# 初始化log，可以直接使用，单例模式
logger = get_logger(**settings.API_LOG_CONFIG)

# 初始化db，可以直接使用，单例模式
db = DB(settings.DB_CONFIG)
