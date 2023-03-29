import sys


def get_opts(name):
    '''
    获取传入的命令行参数
    '''
    args = sys.argv[1:]
    if name in args:
        return args[args.index(name) + 1]
    else:
        return ''


# if __name__ == '__main__':
#     res = get_opts('-m')
#     print(res)
