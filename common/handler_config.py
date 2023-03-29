from configparser import ConfigParser

import yaml


# def get_config(filename, encoding='utf-8') -> dict:
#     # 1、获取文件名后缀
#     suffix = filename.split('.')[-1]
#
#     # 2、判断这个配置文件的类型
#     if suffix in ['ini', 'cfg', 'cnf']:
#         # ini配置
#         conf = ConfigParser()
#         conf.read(filename, encoding=encoding)
#
#         data = {}
#         for section in conf.sections():
#             data[section] = dict(conf.items(section))
#
#     elif suffix in ['yml', 'yaml']:
#         # yaml配置
#         with open(filename, 'r', encoding=encoding) as f:
#             data = yaml.load(f, Loader=yaml.FullLoader)
#     else:
#         raise ValueError('不能识别的配置文件后缀')
#
#     return data


class Config:
    def __init__(self, filename, encoding='utf-8') -> dict:
        self.filename = filename
        self.encoding = encoding
        self.suffix = filename.split('.')[-1]
        if self.suffix not in ['ini', 'cfg', 'cnf', 'yml', 'yaml']:
            raise ValueError('不能识别的配置文件后缀')

    def __parse_ini(self):
        conf = ConfigParser()
        conf.read(self.filename, encoding=self.encoding)

        data = {}
        for section in conf.sections():
            data[section] = dict(conf.items(section))
        return data

    def __parse_yaml(self):
        with open(self.filename, 'r', encoding=self.encoding) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def parse(self):
        if self.suffix in ['yml', 'yaml']:
            return self.__parse_yaml()
        else:
            return self.__parse_ini()

# if __name__ == '__main__':
#     print(get_config('../config.ini'))
#     print(get_config('../config.yaml'))
#     print(Config('../config.ini').parse())
#     print(Config('../config.yaml').parse())
