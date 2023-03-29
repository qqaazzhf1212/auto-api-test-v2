import requests

from conf import settings
from common import logger


def login(username, password, reg_name=None, _type=None):
    """
    注册用户
    :param mobli_phone:
    :param pwd:
    :param reg_name:
    :param _type:
    :return:
    """
    data = {
        'username': username,
        'password': password
    }
    if reg_name:
        data['reg_name'] = reg_name

    if _type is not None:
        data['type'] = _type

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    url = settings.API_PROJECT_HOST + settings.API_INTERFACE['login']
    # print(data)
    try:
        res = requests.post(url=url, json=data, headers=headers)
        if res.status_code == 200:
            logger.info('登录成功')
        else:
            logger.info('登录失败')
        return res.json()
    except Exception as e:
        logger.info('登录失败')
        raise e


# if __name__ == '__main__':
#     print(login('admin', 'GgLoXoE4j374DurMan1n9wHUcXxZKltib7YbQ2/Rn5tVe/Ub2/p8sPEAWU0VEqgGHGuuCmdcV03BDce236znH'))
