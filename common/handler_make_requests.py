import requests


# print(__name__)

def send_http_requests(url, method, **kwargs) -> requests.Response:
    '''发送http请求'''
    # 把方法名小写话
    method = method.lower()
    # 获取对应的方法
    return getattr(requests, method)(url=url, **kwargs)

    # if method == "get":
    #     res = requests.get(url=url, params=params, json=json, data=data, headers=headers, cookies=cookies)
    # elif method == "post":
    #     res = requests.post(url=url, params=params, json=json, data=data, headers=headers, cookies=cookies)
    # elif method == "put":
    #     res = requests.put(url=url, params=params, json=json, data=data, headers=headers, cookies=cookies)
    # elif method == "patch":
    #     res = requests.patch(url=url, params=params, json=json, data=data, headers=headers, cookies=cookies)
    # elif method == "delete":
    #     res = requests.delete(url=url, params=params, json=json, data=data, headers=headers, cookies=cookies)
    #
    # return res

# if __name__ == '__main__':
#     print(dir(requests))
#     case = {
#         'url': 'http://www.baidu.com',
#         'method': 'get',
#         'headers': '',
#         'json': ''
#     }
#
#     print(send_http_requests(url=case['url'], method=case['method']))
