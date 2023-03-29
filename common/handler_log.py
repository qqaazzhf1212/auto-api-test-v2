import logging


def get_logger(name, filename, mode='a', encoding='utf-8', fmt=None, debug=False):
    # 1、创建日志器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 文件处理器的等级一般比控制要高
    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO

    if fmt is None:
        fmt = '"%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s"'

    # 2、创建日志处理器
    # 创建一个写到文件中的日志处理器
    file_handler = logging.FileHandler(filename=filename, mode=mode, encoding=encoding)
    # 日志器可以设置等级
    file_handler.setLevel(file_level)

    # 创建一个控制台处理器将日志输出到控制台
    console_handler = logging.StreamHandler()
    # 日志处理器也可以设置等级
    console_handler.setLevel(console_level)

    # 3、创建格式化器
    formater = logging.Formatter(fmt=fmt)

    # 4、将格式化器添加到日志处理器上
    console_handler.setFormatter(formater)
    file_handler.setFormatter(formater)

    # 5、将日志处理器添加到日志器上
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# if __name__ == '__main__':
#     logger = get_logger('pyapi', '../results/logs/pyapi.log', debug=True)
#     logger.info('我是一个log')
